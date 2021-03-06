from flask_login import UserMixin
from model.firebaseDB import FireBase_CURSOR


class User(UserMixin):
    def __init__(self, id, user_id, user_pw, user_name, user_auth):
        self.id = id
        self.user_id = user_id
        self.user_pw = user_pw
        self.user_name = user_name
        self.user_auth = user_auth

    def get_id(self):
        return str(self.id)

    @staticmethod
    def get(account_id):
        res = FireBase_CURSOR.get_account(account_id)
        if res == None:
            return None
        else:
            return User(id=res["account_id"], user_id=res["user_id"], user_pw=res["user_pw"], user_name=res["user_name"], user_auth=res["auth"])

    @staticmethod
    def find(user_id, user_pw):
        res = FireBase_CURSOR.login(user_id, user_pw)
        if res == None or res == False:
            return None
        else:
            return User(id=res["account_id"], user_id=res["user_id"], user_pw=res["user_pw"], user_name=res["user_name"], user_auth=res["auth"])

    @staticmethod
    def create(user_id, user_pw, user_name):
        res = FireBase_CURSOR.login(user_id, user_pw)
        if res == None:
            FireBase_CURSOR.create(user_id, user_pw, user_name)
            return True
        else:
            return False
