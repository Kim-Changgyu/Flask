from flask import Flask, Blueprint, render_template

viewer = Blueprint("viewer", __name__)

# 라우팅 경로 지정
@viewer.route("/main")
def main():
    return render_template("index.html")

@viewer.route("/login")
def login():
    return render_template("login.html")