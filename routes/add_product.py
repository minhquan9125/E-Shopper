from flask import Blueprint, render_template, request, url_for, redirect, session
from db import get_connection
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

add_product_bp = Blueprint('add_product', __name__)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@add_product_bp.route("/add-product", methods=['GET', 'POST'])
def add_product():
    if 'username' not in session:
        return redirect(url_for('login.login'))

    error = None
    if request.method == 'POST':
        product_id = request.form.get('id', '').strip()
        title = request.form.get('title', '').strip()
        price = request.form.get('price', '').strip()
        file = request.files.get('image')

        if not product_id or not title or not price or not file:
            error = 'Vui lòng điền đầy đủ id, title, price và ảnh.'
        elif file.filename == '':
            error = 'Vui lòng chọn file ảnh.'
        elif not allowed_file(file.filename):
            error = 'Chỉ cho phép ảnh png, jpg, jpeg, gif.'
        else:
            filename = secure_filename(file.filename)
            save_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'images')
            os.makedirs(save_dir, exist_ok=True)
            file_path = os.path.join(save_dir, filename)
            file.save(file_path)
            image_path = f'images/{filename}'

            user_id = session['username']['id']
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO product (id_user, id, title, price, image) VALUES (%s, %s, %s, %s, %s)",
                (user_id, product_id, title, price, image_path),
            )
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('my_products'))

    return render_template('add-product.html', error=error)
