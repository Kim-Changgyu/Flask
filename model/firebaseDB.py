import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(
    "model/flask-a4094-firebase-adminsdk-b5hre-6370423c4e.json")
firebase_admin.initialize_app(
    cred, {'databaseURL': "https://flask-a4094-default-rtdb.firebaseio.com/"})

# 초기 관리자용 계정 설정
# dir = db.reference()
# dir.update({"Account_Count": 1})
# dir.update(
# {"Account": [{"account_id": 0, "user_id": "admin", "user_pw": "admin"}]})


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
            if user_id == account["user_id"] and user_pw == account["user_pw"]:
                return account
            else:
                return False
