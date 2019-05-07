from flask import jsonify
from dao.user import UserDAO

class UserHandler:

    def build_human_dict(self,row):
        result = {}
        result['huid'] = row[0]
        result['hufirst_name'] = row[1]
        result['hulast_name'] = row[2]
        result['hubirthdate'] = row[3]
        result['huemail'] = row[4]
        result['hupassword'] = row[5]
        result['huphone'] = row[6]
        result['huusername'] = row[7]
        return result

    def build_human_attributes(self, huid, huusername, huemail, hupassword, hubirthdate, hufirst_name, hulast_name, huphone):
        result = {}
        result['huid'] = huid
        result['hufirst_name'] = hufirst_name
        result['hulast_name'] = hulast_name
        result['hubirthdate'] = hubirthdate
        result['huemail'] = huemail
        result['hupassword'] = hupassword
        result['huphone'] = huphone
        result['huusername'] = huusername
        return result

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uname'] = row[1]
        result['ucreationDate'] = row[2]
        result['urecentLogin'] = row[3]
        result['first_name']=row[4]
        result['last_name']=row[5]
        result['profile_picture'] = row[6]
        return result

    def build_user_attributes(self, uid, uname, ucreationDate, urecentLogin):
        result = {}
        result['uid'] = uid
        result['uname'] = uname
        result['ucreationDate'] = ucreationDate
        result['urecentLogin'] = urecentLogin
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

    def build_friend_dict(self,row):
        result = {}
        result['fuid']=row[0]
        result['userid']=row[1]
        result['friendid']=row[2]
        return result

    def build_friend_attributes(self,fuid,uid,fuid2):
        result = {}
        result['fuid']=fuid
        result['userid']=uid
        result['friendid']=fuid2
        return result

    def build_friend_email_dict(self,row):
        result = {}
        result['fuid']=row[0]
        result['userid']=row[1]
        result['email']=row[2]
        return result

    def build_friend_email_attributes(self,fuid,uid,email):
        result = {}
        result['fuid'] = fuid
        result['userid'] = uid
        result['email'] = email
        return result

    def registerHumanandcreateuser(self, form):
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
                huid = dao.registerHuman(first_name,last_name,birth_date,email,password,phone,username)
                result = self.build_human_attributes(huid,first_name,last_name,birth_date,email,password,phone,username)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Malformed Post Request"), 400

    def registerFriendByUserId(self,form):
        if len(form) != 2:
            return jsonify(Error="Malformed Post Request"), 400
        else:
            userid = form['uid']
            friendid = form['fuid']
            if userid and friendid:
                dao = UserDAO()
                fuid = dao.registerFriendByUserId(userid,friendid)
                result = self.build_friend_attributes(fuid,userid,friendid)
                return jsonify(Friend=result),201
            else:
                return jsonify(Error="Malformed Post Request"), 400

    def registerFriendByUserEmail(self,form):
        if len(form) != 2:
            return jsonify(Error="Malformed Post Request"), 400
        else:
            userid = form['uid']
            email = form['email']
            if userid and email:
                dao = UserDAO()
                fuid = dao.registerFriendByUserEmail(userid,email)
                result = self.build_friend_email_attributes(fuid,userid,email)
                return jsonify(Friend=result),201
            else:
                return jsonify(Error="Malformed Post Request"), 400


    def deleteFriendById(self,fuid):
        dao = UserDAO()
        if not dao.getFriendByUserId(fuid):
            return jsonify(Error="User not found."), 404
        else:
            dao.deleteFriendById(fuid)
        return jsonify(DeleteStatus="OK"), 200

    def deleteFriendByName(self,fname):
        dao = UserDAO()
        if not dao.getFriendByUserName(fname):
            return jsonify(Error="User not found."), 404
        else:
            dao.deleteFriendByName(fname)
        return jsonify(DeleteStatus="OK"), 200


    def signInUser(self, form):
        username = form['username']
        password = form['password']
        dao = UserDAO()
        result = dao.signInUser(username, password)
        dict_map = self.build_userinfo_dict(result)
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

    def getOwnerOfGroupChatById(self, groupchatid):
        dao = UserDAO()
        row = dao.getOwnerOfGroupChatById(groupchatid)
        if not row:
            return jsonify(Error="Owner not found"), 404
        else:
            owner = self.build_user_dict(row)
            return jsonify(Owner=owner)

    def getUserInformationByUsername(self, username):
        dao = UserDAO()
        result = dao.getUserInformationByUsername(username)
        if result is None:
            return jsonify(Error="User doesn't exist!")
        else:
            result_map = self.build_userinfo_dict(result)
        return jsonify(Users=result_map)


    def deleteAccount(self,uid):
        dao = UserDAO()
        if not dao.getUserByUserId(uid):
            return jsonify(Error="User not found."), 404
        else:
            dao.deleteAccount(uid)
        return jsonify(DeleteStatus="OK"), 200