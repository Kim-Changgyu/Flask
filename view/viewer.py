from flask import Flask, Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
from nbformat import current_nbformat
from control.user_mgmt import User

viewer = Blueprint("viewer", __name__)

# 라우팅 경로 지정


@viewer.route("/main")
def main():
    if current_user.is_authenticated:
        return render_template("index.html", login_status=True, user_id=current_user.user_id)
    else:
        return render_template("index.html")


@viewer.route("/login")
def login():
    return render_template("login.html")


@viewer.route("/login_request")
def login_request():
    if request.method == "GET":
        user = User.find("admin", "admin")
        login_user(user)
        print(current_user.user_id, current_user.user_pw)

        return redirect(url_for("viewer.main"))
