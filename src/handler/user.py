from flask import jsonify
from dao.user import UserDAO

class UserHandler:
    def build_human_dict(self,row):
        result = {}
        result['huid'] = row[0]
        result['huname'] = row[1]
        result['huemail'] = row[2]
        result['hupassword'] = row[3]
        result['hubirthDate'] = row[4]
        result['huphoneNum'] = row[5]
        return result

    def build_user_dict(self,row):
        result = {}
        result['uid'] = row[0]
        result['uname'] = row[1]
        result['unumberPosts'] = row[2]
        result['urecentLogin'] = row[3]
        return result

    def createNewUser(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            huname = form['huname']
            huemail = form['huemail']
            hupassword = form['hupasword']
            hubirthDate = form['hubirthDate']
            huphoneNum = form['huphoneNum']


    def getUserbyId(self,huname):
        dao = UserDAO()
        row = dao.UserDao(huname)
        if not row:
            return jsonify(Error="Chat Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)


    def getAllUsers(self):
        dao = UserDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)

        return jsonify(Users=result_list)

