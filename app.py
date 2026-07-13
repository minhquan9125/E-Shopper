from flask import Flask, render_template, session, redirect, url_for
from routes.register import register_bp
from routes.login import login_bp
from routes.account import account_bp
app = Flask(__name__)
app.secret_key = "super_secret_key"
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(account_bp)

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


@app.route('/my-products')
def my_products():
    print("My Product SESSION =", session)
    return render_template('my-product.html')


if __name__ == '__main__':
    app.run(debug=True)
