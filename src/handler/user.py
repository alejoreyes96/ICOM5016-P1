from flask import jsonify
from dao.user import UserDAO

class UserHandler:

    def build_human_dict(self,row):
        result = {}
        result['huid'] = row[0]
        result['huname'] = row[1]
        result['huemail'] = row[2]
        result['hupassword'] = row[3]
        result['hubirthdate'] = row[4]
        result['hufirst_name'] = row[5]
        result['hulast_name'] = row[6]
        result['huphone'] = row[7]
        return result

    def build_human_attributes(self, huid, huname, huemail, hupassword, hubirthdate, hufirst_name, hulast_name, huphone):
        result = {}
        result['huid'] = huid
        result['huname'] = huname
        result['huemail'] = huemail
        result['hupassword'] = hupassword
        result['hubirthdate'] = hubirthdate
        result['hufirst_name'] = hufirst_name
        result['hulast_name'] = hulast_name
        result['huphone'] = huphone
        return result

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uname'] = row[1]
        result['ucreationDate'] = row[2]
        result['urecentLogin'] = row[3]
        result['first_name'] = row[4]
        result['last_name'] = row[5]
        return result

    def build_user_attributes(self, uid, uname, ucreationDate, urecentLogin, first_name, last_name):
        result = {}
        result['uid'] = uid
        result['uname'] = uname
        result['ucreationDate'] = ucreationDate
        result['urecentLogin'] = urecentLogin
        result['first_name'] = first_name
        result['last_name'] = last_name
        return result

    def build_userinfo_dict(self, row):
        result = {}
        result['huid'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['birthdate'] = row[3]
        result['huemail'] = row[4]
        result['phone_number'] = row[5]
        result['uid'] = row[6]
        result['user_name'] = row[7]
        result['ucreation_date'] = row[8]
        result['umost_recent_login'] = row[9]
        return result

    def build_groupChat_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['gcreationDate'] = row[2]
        result['guserList'] = row[3]
        result['gmediaList'] = row[4]
        result['gowner'] = row[5]
        return result

    def registerHuman(self, form):
        if len(form) != 7:
            return jsonify(Error="Malformed Post Request"), 400
        else:
            username = form['username']
            password = form['password']
            birth_date = form['birth_date']
            first_name = form['first_name']
            last_name = form['last_name']
            email = form['email']
            phone = form['phone']
            if username and password and birth_date and first_name and last_name and email and phone:
                dao = UserDAO()
                huid = dao.registerHuman(username, email, password, birth_date, first_name, last_name, phone)
                result = self.build_human_attributes(huid, username, email, password, birth_date, first_name, last_name, phone)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Malformed Post Request"), 400

    def signInUser(self, form):
        username = form['username']
        password = form['password']
        dao = UserDAO()
        result = dao.signInUser(username, password)
        dict_map = self.build_user_dict(result)
        return jsonify(Users=dict_map)

    def getAllUsers(self):
        dao = UserDAO()
        user_list = dao.getAllUsers()
        result_map = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_map.append(result)
        return jsonify(Users=result_map)

    def getUserByUserId(self, userid):
        dao = UserDAO()
        result = dao.getUserByUserId(userid)
        if result is None:
            return jsonify(Error="User doesn't exist!")
        else:
            result_map = self.build_user_dict(result)
        return jsonify(Users=result_map)

    def getUserInformationByUserId(self, userid):
        dao = UserDAO()
        result = dao.getUserInformationByUserId(userid)
        if result is None:
            return jsonify(Error="User doesn't exist!")
        else:
            result_map = self.build_userinfo_dict(result)
        return jsonify(Users=result_map)

    def getUserInformationByUsername(self, username):
        dao = UserDAO()
        result = dao.getUserInformationByUsername(username)
        if result is None:
            return jsonify(Error="User doesn't exist!")
        else:
            result_map = self.build_userinfo_dict(result)
        return jsonify(Users=result_map)

    def getUserContactsByUserId(self, userid):
        dao = UserDAO()
        user_list = dao.getUserContactsByUserId(userid)
        result_map = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_map.append(result)
        return jsonify(Users=result_map)

    def getUserByUsername(self, username):
        dao = UserDAO()
        result = dao.getUserByUsername(username)
        if result is None:
            return jsonify(Error="User doesn't exist")
        else:
            result_map = self.build_user_dict(result)
        return jsonify(Users=result_map)

    def getUserContactsByUsername(self, username):
        dao = UserDAO()
        user_list = dao.getUserContactsByUsername(username)
        if user_list is None:
            return jsonify(Error="User doesn't have contacts")
        else:
            result_map = []
            for row in user_list:
                result = self.build_user_dict(row)
                result_map.append(result)
            return jsonify(Users=result_map)

    def getGroupChatsByUserId(self, userid):
        dao = UserDAO()
        result = dao.getGroupChatsByUserId(userid)
        result_map = []
        for r in result:
            result_map.append(self.build_groupChat_dict(r))
        return jsonify(GroupChats=result_map)

    def getUsersInGroupChatByUserIdAndGroupChatId(self, userid, groupchatid):
        dao = UserDAO()
        result = dao.getUsersInGroupChatByUserIdAndGroupChatId(userid, groupchatid)
        result_map = []
        for r in result:
            result_map.append(self.build_user_dict(r))
        return jsonify(Users=result_map), 201

    # def createNewUser(self, userName, form):
    #     # print("form: ", form)
    #     # if len(form) != 4:
    #     #     return jsonify(Error="Malformed post request"), 400
    #     # else:
    #         huname = userName
    #         huemail = 'John.Doe@gmail.com'
    #         hupassword = 'JohnDoe1357'
    #         hubirthDate = '27/5/1993'
    #         huphoneNum = '787-938-8539'
    #         if huname and huemail and hupassword and hubirthDate and huphoneNum:
    #             dao = UserDAO()
    #             huid = dao.insert(huname, huemail, hupassword, hubirthDate, huphoneNum)
    #             result = self.build_human_attributes(huid, huname, huemail, hupassword, hubirthDate, huphoneNum)
    #             return jsonify(User=result), 201
    #         else:
    #             return jsonify(Error="Unexpected attributes in post request"), 400

    # def updateUser(self, huid, form):
    #     dao = UserDAO()
    #     if not dao.getUserById(huid):
    #         return jsonify(Error="User not found"), 404
    #     else:
    #         # if len(form) != 4:
    #         #     return jsonify(Error="Malformed post request"), 400
    #         # else:
    #
    #             # if huname and huemail and hupassword and hubirthDate and huphoneNum:
    #                 updated = dao.update(huid)
    #                 result = self.build_user_attributes(updated[0], updated[1], updated[2], updated[3])
    #                 return jsonify(User=result), 200
    #             # else:
    #             #     return jsonify(Error="Unexpected attributes in post request"), 400

    # def getUserbyId(self,uid):
    #     dao = UserDAO()
    #     row = dao.getUserById(uid)
    #     if not row:
    #         return jsonify(Error="User Not Found"), 404
    #     else:
    #         user = self.build_user_dict(row)
    #         return jsonify(User=user)
    #
    #
    # def getAllUsers(self):
    #     dao = UserDAO()
    #     users_list = dao.getAllUsers()
    #     result_list = []
    #     for row in users_list:
    #         result = self.build_user_dict(row)
    #         result_list.append(result)
    #
    #     return jsonify(Users=result_list)
    #
    # def deleteuser(self, uid):
    #     dao = UserDAO()
    #     if not dao.getUserById(uid):
    #         return jsonify(Error="Group Chat not found."), 404
    #     else:
    #         dao.delete(uid)
    #         return jsonify(DeleteStatus="OK"), 200