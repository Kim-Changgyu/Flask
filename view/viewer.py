from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user
from nbformat import current_nbformat
from control.user_mgmt import User
from model.firebaseDB import FireBase_CURSOR
import datetime

viewer = Blueprint("viewer", __name__)

# 라우팅 경로 지정


@viewer.route("/main")
def main():
    notices = FireBase_CURSOR.load_notices()

    if current_user.is_authenticated:
        return render_template("index.html", login_status=current_user.user_auth, user_name=current_user.user_name, notices=notices)
    else:
        return render_template("index.html", notices=notices)


@viewer.route("/login")
def login():
    return render_template("login.html")


@viewer.route("/login_request")
def login_request():
    if request.method == "GET":

        user = User.find(str(request.args.get("user_id")),
                         str(request.args.get("user_pw")))

        if user == None:
            flash("계정 정보가 올바르지 않습니다.")
        else:
            if request.args.get("remember") == None:
                login_user(user)
            else:
                login_user(user, remember=True,
                           duration=datetime.timedelta(days=30))

        return redirect(url_for("viewer.main"))


@viewer.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("viewer.main"))


@viewer.route("/signin")
def signin():
    return render_template("signup.html")


@viewer.route("/signup_request", methods=["POST"])
def signup_request():
    if request.method == "POST":
        new_user = User.create(str(request.form["user_id"]), str(
            request.form["user_pw"]), str(request.form["user_name"]))

        if new_user == True:
            flash("회원가입이 완료 됐습니다.")
        else:
            flash("이미 존재하는 계정이거나 회원가입 과정에서 문제가 발생했습니다.")

        return redirect(url_for("viewer.main"))
