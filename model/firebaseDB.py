import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(
    "model/flask-a4094-firebase-adminsdk-b5hre-6370423c4e.json")
firebase_admin.initialize_app(
    cred, {'databaseURL': "https://flask-a4094-default-rtdb.firebaseio.com/"})


class FireBase_CURSOR:
    @staticmethod
    def get_account(id):
        accounts = db.reference().get()["Account"]

        for account in accounts:
            if int(account["account_id"]) == int(id):
                return account

        return None

    @staticmethod
    def login(user_id, user_pw):
        accounts = db.reference().get()["Account"]

        for account in accounts:
            if user_id == account["user_id"]:
                if user_pw == account["user_pw"]:
                    return account
                else:
                    return False

        return None

    @staticmethod
    def create(user_id, user_pw, user_name):
        accounts = db.reference().get()["Account"]
        accounts.append({
            "account_id": len(accounts),
            "user_id": str(user_id),
            "user_pw": str(user_pw),
            "user_name": str(user_name),
            "auth": "guest"
        })
        db.reference().update({"Account": accounts})

    @staticmethod
    def load_notices():
        return db.reference().get()["Notice"]


# 초기 관리자용 계정 설정
# dir = db.reference()
# dir.update(
#     {"Account": [{"account_id": 0, "user_id": "admin", "user_pw": "admin", "auth": "admin", "user_name": "관리자"}]})


# 공지사항 데이터 전송
# notices = {"2022-01-16": ["부트스트랩(Bootstrap) 프레임워크로 헤더 예제 적용", "웹 서버 실행 파일 구현 & 라우팅 테스트"],
#            "2022-01-17": ["Flask 블루프린트 기능을 활용한 라우팅 모듈화", "Firebase 원격 데이터베이스 구축 & 연동"],
#            "2022-01-18": ["임시 로그인 기능 & 상태 유지 추가"],
#            "2022-01-19": ["ID/PW 로그인 기능 추가 & 로그아웃 기능 추가", "개발노트 (공지사항) 데이터베이스화"],
#            "2022-01-20": ["회원가입 기능 추가"]}
# dir = db.reference()
# dir.update({"Notice": notices})
