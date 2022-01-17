import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("model/flask-a4094-firebase-adminsdk-b5hre-6370423c4e.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://flask-a4094-default-rtdb.firebaseio.com/"})

# 초기 관리자용 계정 설정
# dir = db.reference()
# dir.update({"account": {"admin": "admin"}})

def get(user_id, user_pw):
    res = db.reference().get()["account"]
    
    if user_id in res.keys():
        if res[user_id] == user_pw:
            return True
        else:
            return False
    else:
        return None