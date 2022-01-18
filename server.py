from distutils.log import Log, debug
from flask import Flask, render_template, make_response, jsonify
from flask_login import LoginManager
from flask_cors import CORS
from view import viewer
from control.user_mgmt import User

# Flask 객체 생성
app = Flask(__name__)
CORS(app)                   # Cross Origin Resource Sharing
app.secret_key = "test"

# Blueprint 등록 (라우팅 경로 모듈화)
app.register_blueprint(viewer.viewer, url_prefix="/flask")
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"


@login_manager.user_loader
def load_user(account_id):
    return User.get(account_id)


@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)


# 서버 시작
if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)
