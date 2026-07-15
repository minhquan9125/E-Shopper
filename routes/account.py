from flask import request, session, render_template, redirect, url_for, Blueprint
from werkzeug.security import generate_password_hash
import re
from db import get_connection


account_bp = Blueprint('account_bp', __name__)


@account_bp.route('/account', methods=['GET', 'POST'])
def account():
    message = {}
    email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    

    if 'username' not in session:
        return redirect(url_for('login.login'))
    
    if request.method == 'POST':
        name_new = request.form.get('name', '').strip()
        email_new = request.form.get('email', '').strip()
        password_new = request.form.get('password', '').strip()

        if not name_new:
            message['name_new'] = "Vui lòng nhập họ tên mới."
            
        if not email_new:
            message['email_new'] = "Vui lòng nhập email mới."
        elif not re.match(email_pattern, email_new):
            message['email_new'] = "Email không đúng định dạng hợp lệ."
            
        if not password_new:
            message['password_new'] = "Vui lòng nhập mật khẩu mới."
        elif len(password_new) < 6:
            message['password_new'] = "Mật khẩu mới phải từ 6 ký tự trở lên."

        if not message:
            user_id = session.get('username', {}).get('id')
            
            hash_password = generate_password_hash(password_new)
            
            con = get_connection()
            cur = con.cursor()

            try:   
                cur.execute("UPDATE member SET name = %s, email = %s, password = %s WHERE id_user = %s", 
                            (name_new, email_new, hash_password, user_id))
                con.commit()
                
                session['username'] = {
                    'id': user_id,
                    'email': email_new
                }
                
                message['success'] = "Cập nhật tài khoản thành công!"
                
            except Exception as e:
                con.rollback() 
                message['error'] = f"Lỗi hệ thống: {str(e)}"
            finally:

                cur.close()
                con.close()

    return render_template('account.html', message=message)