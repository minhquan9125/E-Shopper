from flask import Blueprint, request, render_template, session, redirect, url_for

form_bp = Blueprint("form", __name__)

@form_bp.route("/form", methods=["GET", "POST"])
def form():
    email = ""
    password = ""
    city = ""
    error = {}

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        city = request.form.get("city", "").strip()

        if not email:
            error["email"] = "Vui lòng nhập email"

        elif not password:
            error["password"] = "Vui lòng nhập password"

        elif not city:
            error["city"] = "Vui lòng nhập city"

        if not error:
            new_entry = {
                "email": email,
                "password": password,
                "city": city
            }
            if "form" not in session:
                session["form"] = []
            session["form"].append(new_entry)
            session.modified = True

            return redirect(url_for("form.table"))

    return render_template(
        "form.html",
        email=email,
        password=password,
        city=city,
        error=error
    )
@form_bp.route("/table")
def table():
    session_data = session.get("form", [])
    return render_template("table.html", session_data=session_data)
