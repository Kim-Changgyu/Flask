from distutils.log import debug
from flask import Flask, render_template
from flask_cors import CORS

# Flask 객체 생성
app = Flask(__name__)
CORS(app)                   # Cross Origin Resource Sharing

# 테스트를 위한 라우팅 경로 (main)
@app.route("/main")
def main():
    return render_template("index.html")

# 서버 시작
if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)