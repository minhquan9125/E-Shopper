from flask import Blueprint,request, render_template ,session,redirect,url_for
import re
from db import get_connection
from werkzeug.security import generate_password_hash,check_password_hash
login_bp= Blueprint('login',__name__)

@login_bp.route('/login', methods =['GET' , 'POST'] )


def login():
    error={}
    message=''
    email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if request.method== 'POST' :
        email = request.form.get('email','').strip()
        password= request.form.get('password')

        if not email:
            error['email'] = " Vui long nhap email "
        if not re.match(email_pattern,email) :
            error['email'] = " Vui long dung dang email  "
        if not password:
            error['password'] = " Vui long nhap email "
        if not error :
            con = get_connection()
            cur=con.cursor()
            cur.execute("SELECT *  FROM member where email=%s ",
                    (email,)
                    )
            member = cur.fetchone()
            if member:
                print("Password nhập:", password)
                print("Hash DB:", member['password'])
                print("Check:", check_password_hash(member['password'], password))
        
            con.commit()
            cur.close()
            con.close()
            if member and check_password_hash(member['password'], password):
                session['username'] = {
                    'id': member['id_user'],
                    'email': member['email'],
                }
            else:
                error['login_failed'] = "Sai tài khoản hoặc mật khẩu"

            return redirect("/")

    return render_template('login.html', error=error ,message=message)