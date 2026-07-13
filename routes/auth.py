import os
import re
import uuid
from flask import Blueprint, render_template, request, current_app
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

auth_bp = Blueprint("login", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
MAX_SIZE = 1 * 1024 * 1024  
MAX_FILES = 3


def is_check_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email) is not None


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    email = ""
    hashed_password = ""
    success = ""
    uploaded_files = []

    error = {}

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        files = request.files.getlist("avatar")

        if not email:
            error["email"] = "Vui lòng nhập email"

        elif not is_check_email(email):
            error["email"] = "Email không đúng định dạng"

       
        if not password:
            error["password"] = "Vui lòng nhập password"

        elif len(password) < 6:
            error["password"] = "Password phải có ít nhất 6 ký tự"

        # ======================
        # Validate File
        # ======================
        valid_files = [f for f in files if f.filename != ""]

        if len(valid_files) == 0:
            error["file"] = "Vui lòng chọn file"

        elif len(valid_files) > MAX_FILES:
            error["file"] = "Chỉ được upload tối đa 3 file"

        else:
            for file in valid_files:

                if not allowed_file(file.filename):
                    error["file"] = "Chỉ chấp nhận PNG, JPG, JPEG, GIF"
                    break

                file.seek(0, os.SEEK_END)
                file_size = file.tell()
                file.seek(0)

                if file_size > MAX_SIZE:
                    error["file"] = f"{file.filename} vượt quá 1MB"
                    break

        # ======================
        # Save
        # ======================
        if not error:

            hashed_password = generate_password_hash(password)

            upload_folder = os.path.join(current_app.root_path, "uploads")
            os.makedirs(upload_folder, exist_ok=True)

            for file in valid_files:
                filename = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
                file.save(os.path.join(upload_folder, filename))
                uploaded_files.append(filename)

            success = "Đăng nhập và upload thành công!"

    return render_template(
        "login.html",
        email=email,
        error=error,
        hashed_password=hashed_password,
        success=success,
        uploaded_files=uploaded_files
    )

from flask import Blueprint, render_template, request, session, current_app
import os
import re
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

register_bp = Blueprint("register", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
MAX_FILE_SIZE_MB = 1


def allowed_file(filename):
    return ("." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS)


def CheckEmail(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email) is not None


@register_bp.route("/register", methods=["GET", "POST"])
def register():

    email = ""
    password = ""
    hashed_password = ""
    file = ""

    error = {}

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        file = request.files.get("avatar")

        # Email
        if not email:
            error["email"] = "Vui lòng nhập email."
        elif not CheckEmail(email):
            error["email"] = "Email không đúng định dạng."

        # Password
        if not password:
            error["password"] = "Vui lòng nhập mật khẩu."

        # File
        if not file or file.filename == "":
            error["file"] = "Vui lòng chọn ảnh."

        elif not allowed_file(file.filename):
            error["file"] = "Chỉ chấp nhận png, jpg, jpeg, gif."

        else:
            file.seek(0, os.SEEK_END)
            file_size = file.tell()
            file.seek(0)

            if file_size > MAX_FILE_SIZE_MB * 1024 * 1024:
                error["file"] = "File vượt quá 1MB."

        if not error:

            hashed_password = generate_password_hash(password)

            upload_folder = os.path.join(current_app.root_path, "uploads")

            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_folder, filename))

            session["Username"] = {
                "email": email,
                "password": hashed_password ,
                "avatar": filename
            }

            print(session["Username"])

    return render_template(
        "register.html",
        email=email,
        error=error,
        hashed_password=hashed_password
    )