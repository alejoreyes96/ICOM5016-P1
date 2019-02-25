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

    def build_user_dict(self, row):
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


    def updateNewUser(self,huid, form):
        dao = UserDAO()
        if not dao.getGroupChatById(huid):
            return jsonify(Error="GroupChat not found"), 404
        else:
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
                    huid = dao.update(huname, huemail, hupassword, hubirthDate, huphoneNum)
                    result = self.build_user_attributes(huid, huname, huemail, hupassword, hubirthDate, huphoneNum)
                    return jsonify(User=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def getUserbyId(self,uid):
        dao = UserDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error="User Not Found"), 404
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

    def deleteuser(self, uid):
        dao = UserDAO()
        if not dao.getUserById(uid):
            return jsonify(Error="Group Chat not found."), 404
        else:
            dao.delete(uid)
            return jsonify(DeleteStatus="OK"), 200
