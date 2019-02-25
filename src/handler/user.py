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

    def build_human_attributes(self, huid, huname, huemail, hupassword, hubirthDate, huphoneNum):
        result = {}
        result['huid'] = huid
        result['huname'] = huname
        result['huemail'] = huemail
        result['hupassword'] = hupassword
        result['hubirthDate'] = hubirthDate
        result['huphoneNum'] = huphoneNum
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
            if huname and huemail and hupassword and hubirthDate and huphoneNum:
                dao = UserDAO()
                huid = dao.insert(huname, huemail, hupassword, hubirthDate, huphoneNum)
                result = self.build_user_attributes(huid, huname, huemail, hupassword, hubirthDate, huphoneNum)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400



    def getUserbyId(self, uname):
        dao = UserDAO()
        user_list = dao.getUserById(uname)
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)

        return jsonify(User=result_list)

    def getAllUsers(self):
        dao = UserDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)

        return jsonify(Users=result_list)