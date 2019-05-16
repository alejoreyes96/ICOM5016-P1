from flask import jsonify
from dao.user import UserDAO
import datetime as dt
from config.dbconfig import pg_config

class UserHandler:

    def build_human_dict(self,row):
        result = {}
        result['uid'] = row[0]
        result['hufirst_name'] = row[1]
        result['hulast_name'] = row[2]
        result['hubirthdate'] = row[3]
        result['huemail'] = row[4]
        result['hupassword'] = row[5]
        result['huphone'] = row[6]
        result['huusername'] = row[7]
        return result

    def build_human_attributes(self, uid, huusername, huemail, hupassword, hubirthdate, hufirst_name, hulast_name, huphone):
        result = {}
        result['uid'] = uid
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

    def build_user_update_attributes(self, uid, uname,urecentLogin,picture):
        result = {}
        result['uid'] = uid
        result['uname'] = uname
        result['urecentLogin'] = urecentLogin
        result['profile_picture'] = picture
        return result

    def build_userinfo_dict(self, row):
        result = {}
        result['huid'] = row[0]
        result['profile_picture'] = row[1]
        result['first_name'] = row[2]
        result['last_name'] = row[3]
        result['birthdate'] = row[4]
        result['huemail'] = row[5]
        result['phone_number'] = row[6]
        result['uid'] = row[7]
        result['user_name'] = row[8]
        result['ucreation_date'] = row[9]
        result['umost_recent_login'] = row[10]
        result['hupassword'] = row[11]
        return result

    def build_userinfo_attributes(self, huid,first_name,last_name,birthdate,huemail,phone_number,uid,
                                  user_name,ucreation_date,umost_recent_login):
        result = {}
        result['huid'] = huid
        result['first_name'] = first_name
        result['last_name'] = last_name
        result['birthdate'] = birthdate
        result['huemail'] = huemail
        result['phone_number'] = phone_number
        result['uid'] = uid
        result['user_name'] = user_name
        result['ucreation_date'] = ucreation_date
        result['umost_recent_login'] = umost_recent_login
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

    def registerHumanAndCreateUser(self, form):
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
                uid = dao.registerHumanAndCreateUser(first_name,last_name,birth_date,email,password,phone,username)
                result = self.build_human_attributes(uid,username,email,password,birth_date,first_name,last_name,phone)
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

    def registerFriendByUserEmail(self,uid,form):
        if len(form) != 1:
            return jsonify(Error="Malformed Post Request"), 400
        else:
            email = form['email']
            if email:
                dao = UserDAO()
                if dao.getUserByUserEmail(email) is not None:
                    fuid = dao.registerFriendByUserEmail(uid,email)
                    result = self.build_friend_email_attributes(fuid,uid,email)
                    return jsonify(Friend=result),201
                else:
                    return jsonify(Error="User Not Found"), 404
            else:
                return jsonify(Error="Malformed Post Request"), 400


    def deleteFriendById(self,fuid):
        dao = UserDAO()
        if not dao.getFriendByUserId(fuid):
            return jsonify(Error="User not found."), 404
        else:
            dao.deleteFriendById(fuid)
        return jsonify(DeleteStatus="OK"), 200

    def deleteFriendByName(self,uid,form):
        if len(form)!=1:
            return jsonify(Error="Malformed Post Request"), 400
        else:
            fname=form['fname']
            dao = UserDAO()
            if dao.getFriendByUserName(fname) is None:
                return jsonify(Error="User not found."), 404
            else:
                dao.deleteFriendByName(fname)
            return jsonify(DeleteStatus="OK"), 200

    def signInUser(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed Post Request"), 400
        else:
            username = form['user_name']
            password = form['password']
            dao = UserDAO()
            if username and password:
                result = dao.signInUser(username, password)
                if result is None:
                    return jsonify(Error="User not found."), 404
                else:
                    dict_map = self.build_user_dict(result)
                    return jsonify(Users=dict_map)
            else:
                return jsonify(Error="Malformed Post Request"), 400


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
        result_map = []
        for r in row:
            result_map.append(self.build_user_dict(r))
        return jsonify(Owner=result_map)

    def getUserInformationByUsername(self, username):
        dao = UserDAO()
        result = dao.getUserInformationByUsername(username)
        if result is None:
            return jsonify(Error="User doesn't exist!")
        else:
            result_map = self.build_userinfo_dict(result)
        return jsonify(Users=result_map)

    def updateUser(self, uid, form):
        dao = UserDAO()
        if not dao.getUserByUserId(uid):
                return jsonify(Error="User not found."), 404
        else:
            if len(form) != 8:
                return jsonify(Error="Malformed update request"), 400
            else:
                username = form['username']
                password = form['password']
                birth_date = form['birth_date']
                first_name = form['first_name']
                last_name = form['last_name']
                email = form['email']
                phone = form['phone']
                profile_picture = form['profile_picture']
                date = dt.datetime.now().strftime("%m/%d/%Y")
                if profile_picture and phone and email and last_name and first_name and birth_date and username \
                        and password:
                    dao.updateUser(uid,username,password,birth_date,first_name,last_name,email,phone,profile_picture)
                    result = self.build_user_update_attributes(uid,username,date,profile_picture)
                    return jsonify(User=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteAccount(self,uid):
        dao = UserDAO()
        if not dao.getUserByUserId(uid):
            return jsonify(Error="User not found."), 404
        else:
            dao.deleteAccount(uid)
        return jsonify(DeleteStatus="OK"), 200