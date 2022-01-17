from distutils.log import debug
from flask import Flask, render_template
from flask_cors import CORS
from view import viewer

# Flask 객체 생성
app = Flask(__name__)
CORS(app)                   # Cross Origin Resource Sharing

# Blueprint 등록 (라우팅 경로 모듈화)
app.register_blueprint(viewer.viewer, url_prefix="/flask")

# 서버 시작
if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)