from flask import Blueprint, redirect, render_template, request, url_for
import re, os
from werkzeug.security import generate_password_hash

from db import get_connection

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
MAX_FILE_SIZE_MB = 1

register_bp = Blueprint("register", __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    error = {}
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        file = request.files.get('avatar')

        if not username:
            error['username'] = "Vui lòng nhập tên"
        if not email:
            error['email'] = "Vui lòng nhập email"
        elif not re.match(email_pattern, email):
            error['email'] = "Vui lòng nhập đúng định dạng"
        if not password:
            error['password'] = "Vui lòng nhập password"
            
        if not file or file.filename == "":
            error["file"] = "Vui lòng chọn ảnh."   
        else:
            if not allowed_file(file.filename):
                error["file"] = "Chỉ cho phép tải lên các định dạng ảnh (png, jpg, jpeg, gif)."
            else:
                file.seek(0, os.SEEK_END)
                file_size = file.tell()
                file.seek(0)
    
                if file_size > MAX_FILE_SIZE_MB * 1024 * 1024:
                    error["file"] = "File vượt quá dung lượng 1MB." 
            if not error:
                hash_password = generate_password_hash(password)
                conn = get_connection()
                cur = conn.cursor()
                cur.execute(
                "INSERT INTO member(name,email,password,avatar ) VALUES (%s, %s,%s,%s)",
                (username,email,hash_password,file.filename)
                )
                conn.commit()
                cur.close()
                conn.close()
                return redirect(url_for('login.login'))

    return render_template('register.html', error=error)