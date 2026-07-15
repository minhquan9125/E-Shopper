from flask import Flask, render_template, session, redirect, url_for, request
from routes.register import register_bp
from routes.login import login_bp
from routes.account import account_bp
from routes.add_product import add_product_bp
from db import get_connection

app = Flask(__name__)
app.secret_key = "super_secret_key"
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(account_bp)
app.register_blueprint(add_product_bp)

@app.route('/')
def index():
    print("INDEX SESSION =", session)
    return render_template('index.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/blogdetail')
def blogdetail():
    return render_template('blogdetail.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login.login'))


@app.route('/my-product')
def my_products():
    if 'username' not in session:
        return redirect(url_for('login.login'))

    user_id = session['username']['id']
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, price, image FROM product WHERE id_user = %s", (user_id,))
    products = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('my-product.html', products=products)

@app.route('/edit-product/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    if 'username' not in session:
        return redirect(url_for('login.login'))

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        price = request.form.get('price', '').strip()
        image = request.form.get('image', '').strip()

        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE product SET title=%s, price=%s, image=%s WHERE id=%s AND id_user=%s",
            (title, price, image, product_id, session['username']['id']),
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('my_products'))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, price, image FROM product WHERE id=%s AND id_user=%s", (product_id, session['username']['id']))
    product = cur.fetchone()
    cur.close()
    conn.close()

    return render_template('edit-product.html', product=product)

@app.route('/delete-product/<product_id>')
def delete_product(product_id):
    if 'username' not in session:
        return redirect(url_for('login.login'))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM product WHERE id=%s AND id_user=%s", (product_id, session['username']['id']))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('my_products'))



if __name__ == '__main__':
    app.run(debug=True)
