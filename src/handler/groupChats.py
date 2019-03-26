from flask import jsonify
from dao.groupChats import GroupChatsDAO
from dao.user import UserDAO

class ChatHandler:

    def build_message_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['mmessage'] = row[1]
        result['mupload_date'] = row[2]
        result['msize'] = row[3]
        result['mlength'] = row[4]
        result['mtype'] = row[5]
        result['mpath'] = row[6]
        result['uid'] = row[7]
        return result

    def build_messages_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['mmessage'] = row[1]
        result['mupload_date'] = row[2]
        result['msize'] = row[3]
        result['mlength'] = row[4]
        result['mtype'] = row[5]
        result['mpath'] = row[6]
        result['mmedia_path'] = row[7]
        result['uid'] = row[8]
        return result

    def build_message_attributes(self, mid, mmessage, mupload_date, msize, mlength, mtype, mpath, mhashtag):
        result = {}
        result['mid'] = mid
        result['mmessage'] = mmessage
        result['mupload_date'] = mupload_date
        result['msize'] = msize
        result['mlength'] = mlength
        result['mtype'] = mtype
        result['mpath'] = mpath
        result['mhashtag'] = mhashtag

        return result

    def build_groupChat_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['gcreation_date'] = row[2]
        result['gpicture_id'] = row[3]
        return result

    def build_groupChat_attributes(self, gid, gname, gcreation_date, gpicture_id):
        result = {}
        result['gid'] = gid
        result['gname'] = gname
        result['gcreation_date'] = gcreation_date
        result['gpicture_id'] = gpicture_id
        return result

    def build_groupChats_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['gcreation_date'] = row[2]
        result['gpicture_id'] = row[3]
        result['first_name'] = row[4]
        result['last_name'] = row[5]
        result['uid'] = row[6]
        return result

    # def build_creates_dict(self, row):
    #     result = {}
    #     result['chuid'] = row[0]
    #     result['cgid'] = row[1]
    #     return result
    #
    # def build_isMember_dict(self, row):
    #     result = {}
    #     result['igid'] = row[0]
    #     result['iuid'] = row[1]
    #     return result
    #
    # def build_reacts_dict(self, row):
    #     result = {}
    #     result['rrid'] = row[0]
    #     result['rmid'] = row[1]
    #     return result

    def build_reactions_dict(self, row):
        result = {}
        result['rtype'] = row[0]
        result['rid'] = row[1]
        result['uid'] = row[2]
        result['user_name'] = row[3]
        result['rupload_date'] = row[4]
        result['first_name'] = row[5]
        result['last_name'] = row[6]
        return result

    def build_reactions_attributes(self, rid, rtype, rupload_date):
        result = {}
        result['rid'] = rid
        result['rtype'] = rtype
        result['rupload_date'] = rupload_date
        return result

    def build_reply_dict(self, row):
        result = {}
        result['rpid'] = row[0]
        result['rpreply'] = row[1]
        result['rpupload_date'] = row[2]
        result['rphashtag'] = row[3]
        return result

    def build_reply_attributes(self, rpid, rpreply, rpupload_date, rphashtag):
        result = {}
        result['rpid'] = rpid
        result['rpreply'] = rpreply
        result['rpupload_date'] = rpupload_date
        result['rphashtag'] = rphashtag
        return result

    # def build_sends_dict(self, row):
    #     result = {}
    #     result['suid'] = row[0]
    #     result['smid'] = row[1]
    #     return result
    #
    # def build_contains_dict(self, row):
    #     result = {}
    #     result['cmid'] = row[0]
    #     result['chid'] = row[1]
    #     return result
    #
    # def build_replied_dict(self, row):
    #     result = {}
    #     result['rrpid'] = row[0]
    #     result['rmid'] = row[1]
    #     return result
    #
    # def build_makesReply_dict(self, row):
    #     result = {}
    #     result['mrpid'] = row[0]
    #     result['mmid'] = row[1]
    #     return result

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

    def build_likes_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['likes'] = row[1]
        return result

    def build_dislikes_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['dislikes'] = row[1]
        return result

    def getAvailableGroupChatsByUserId(self, userid):
        dao = GroupChatsDAO()
        chat_list = dao.getAvailableGroupChatsByUserId(userid)
        result_map = []
        for row in chat_list:
            result = self.build_groupChats_dict(row)
            result_map.append(result)
        return jsonify(GroupChats=result_map), 201

    def createGroupChat(self, userid, form):
        if len(form) != 2:
            return jsonify(Error="Malformed Post Request"), 400
        else:
            gname = form['gname']
            gpicture_id = form['gpicture_id']
            if gname and gpicture_id:
                dao = GroupChatsDAO()
                response = dao.createGroupChat(userid, gname)
                gid = response[0]
                gcreation_date = response[1]
                result = self.build_groupChat_attributes(gid, gname, gcreation_date, gpicture_id)
                if result is None:
                    return jsonify(Error="Unable to create group chat")
                else:
                    return jsonify(GroupChat=result)

            else:
                return jsonify(Error="Malformed Post Request"), 400

    def getGroupChatById(self, gid):
        dao = GroupChatsDAO()
        chat = dao.getGroupChatById(gid)
        result_map = []
        if not chat:
            return jsonify(Error="Group chat Not Found"), 404
        else:
            result = self.build_groupChats_dict(chat)
            result_map.append(result)
        return jsonify(GroupChat=result_map), 201

    def updateGroupChat(self, gid, json):
         dao = GroupChatsDAO()
         if not dao.getGroupChatById(gid):
             return jsonify(Error="GroupChat not found"), 404
         else:
             if len(json) != 2:
                 return jsonify(Error="Malformed update request"), 400
             else:
                gname = json['gname']
                gpicture_id = json['gpicture_id']

                if gname and gpicture_id:
                     response = dao.updateGroupChat(gid, gname, gpicture_id)
                     result = self.build_groupChat_attributes(gid, gname, response, gpicture_id)
                     return jsonify(GroupChat=result), 200
                else:
                     return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteGroupChat(self, gid):
        dao = GroupChatsDAO()
        if not dao.getGroupChatById(gid):
            return jsonify(Error="Group Chat not found."), 404
        else:
            dao.deleteGroupChat(gid)
            return jsonify(DeleteStatus="OK"), 200


    def getMessagesByHashtagStringInGroupChat(self, userid, groupchatid, hashtagstring):
        dao = GroupChatsDAO()
        result_map = []
        result = dao.getMessagesByHashtagStringInGroupChat(userid, groupchatid, hashtagstring)
        for r in result:
            result_map.append(self.build_message_dict(r))
        return jsonify(Messages=result_map), 201

    def getMessagesFromGroupChatByUserIdAndGroupChatId(self, userid, groupchatid):
        dao = GroupChatsDAO()
        result = dao.getMessagesFromGroupChatByUserIdAndGroupChatId(userid, groupchatid)
        result_map = []
        for r in result:
            result_map.append(self.build_message_dict(r))
        return jsonify(Messages=result_map), 201

    def getMessageReactionsInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid, messageid):
        dao = GroupChatsDAO()
        result = dao.getMessageReactionsInGroupChatByUserIdAndGroupChatIdAndMessageId(userid, groupchatid, messageid)
        result_map = []
        if result is None:
            return jsonify(Error="Unable to get reactions")
        else:
            for r in result:
                result_map.append(self.build_reactions_dict(r))
            return jsonify(Reactions=result_map)

    def addReaction(self, userid, groupchatid, messageid, json):

        dao = GroupChatsDAO()
        if len(json) != 2:
            return jsonify(Error="Malformed update request"), 400
        else:
            rtype = json['rtype']
            rupload_date = json['rupload_date']

            if rtype and rupload_date:
                rid = dao.addReaction(userid, groupchatid, messageid, rtype, rupload_date)
                result = self.build_reactions_attributes(rid, rtype, rupload_date)
                return jsonify(Reaction = result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateReaction(self, groupchatid, messageid, reactionid, json):
        dao = GroupChatsDAO()
        if not dao.getReactionById(groupchatid, messageid, reactionid):
            return jsonify(Error="Message not found"), 404
        else:
            if len(json) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                rtype = json['rtype']
                rupload_date = json['rupload_date']

                if rtype and rupload_date:
                    dao.updateReaction(groupchatid, messageid, reactionid, rtype, rupload_date)
                    result = self.build_reactions_attributes(reactionid, rtype, rupload_date)
                    return jsonify(Reaction=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteReaction(self, groupchatid, messageid, reactionid):
        dao = GroupChatsDAO()
        if not dao.getReactionById(groupchatid, messageid, reactionid):
            return jsonify(Error="Message not found"), 404
        else:
            dao.deleteReaction(groupchatid, messageid, reactionid)
            return jsonify(DeleteStatus="OK"), 200


    def getRepliesFromMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid, messageid):
        dao = GroupChatsDAO()
        result = dao.getRepliesFromMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(userid, groupchatid, messageid)
        result_map = []
        for r in result:
            result_map.append(self.build_reply_dict(r))
        return jsonify(Reactions=result_map)

    def replyToMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid, messageid, form):

        dao = GroupChatsDAO()
        if len(form) != 3:
            return jsonify(Error="Malformed update request"), 400
        else:
            rpreply = form['rpreply']
            rpupload_date = form['rpupload_date']
            rphashtag = form['rphashtag']

            if rpreply and rpupload_date and rphashtag:

                rpid = dao.replyToMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(userid, groupchatid, messageid, rpreply, rpupload_date, rphashtag)
                result = self.build_reply_attributes(rpid, rpreply, rpupload_date, rphashtag)
                return jsonify(Reply=result)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def postMessage(self, uid, gid, json):

            mmessage = json['mmessage']
            mupload_date= json['mupload_date']
            msize = json['msize']
            mlength = json['mlength']
            mtype = json['mtype']
            mpath = json['mpath']
            mhashtag = json['mhashtag']

            if mmessage and mupload_date and msize and mlength and mtype and mpath and mhashtag:
                dao = GroupChatsDAO()
                mid = dao.insertMessage(uid, gid, mmessage, mupload_date, msize, mlength, mtype, mpath, mhashtag)
                result = self.build_message_attributes(mid, mmessage, mupload_date, msize, mlength, mtype, mpath, mhashtag)
                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Malformed Post Request"), 400

    def getMessagesFromGroupChatById(self, gid, uid, mid):
        dao = GroupChatsDAO()
        row = dao.getMessageFromGroupChatById(gid, uid, mid)
        if not row:
            return jsonify(Error="Message Not Found"), 404
        else:
            for row in chat_list:
                result = self.build_groupChats_dict(row)
                result_map.append(result)
        return jsonify(GroupChat=result_map), 201

    def deleteUserFromGroupChatById(self, userid, userid2, groupchatid):
        usersInGroupChat = UserDAO().getUsersInGroupChatByUserIdAndGroupChatId(userid, groupchatid)
        if usersInGroupChat is None or len(usersInGroupChat) == 0:
            return jsonify(Error="User not found in this group chat and/or group chat does not exist.")
        else:
            dao = GroupChatsDAO()
            dao.deleteUserFromGroupChat(userid, userid2, groupchatid)
            return jsonify(DeleteStatus="Ok"), 200

    def getReplyById(self, userid, groupchatid, messageid, replyid):
        dao = GroupChatsDAO()
        row = dao.getReplyById(userid, groupchatid, messageid, replyid)
        if not row:
            return jsonify(Error="Reply Not Found"), 404
        else:
            reply = self.build_reply_dict(row)
            return jsonify(Reply=reply)

    def updateReply(self, userid, groupchatid, messageid, replyid, json):
        dao = GroupChatsDAO()
        if not dao.getReplyById(userid, groupchatid, messageid, replyid):
            return jsonify(Error="Reply Not Found!"), 404
        else:
            if len(json) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                rpreply = json['rpreply']
                rpupload_date = json['rpupload_date']
                rphashtag = json['rphashtag']

                if rpreply and rpupload_date and rphashtag:
                    dao.updateReply(userid, groupchatid, messageid, replyid, rpreply, rpupload_date, rphashtag)
                    result = self. build_reply_attributes(replyid, rpreply, rpupload_date, rphashtag)
                    return jsonify(Reply=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteReply(self, userid, groupchatid, messageid, replyid):
        dao = GroupChatsDAO()
        if not dao.getReplyById(userid, groupchatid, messageid, replyid):
            return jsonify(Error="Reply not found."), 404
        else:
            dao.deleteReply(userid, groupchatid, messageid, replyid)
            return jsonify(DeleteStatus="OK"), 200

    def getAllMessages(self):
        dao = GroupChatsDAO()
        messages = dao.getAllMessages()
        result_map = []
        if not messages:
            return jsonify(Error="No messages to show")
        else:
            for m in messages:
                result_map.append(self.build_message_dict(m))
            return jsonify(Messages=result_map)

    def getAllGroupChats(self):
        dao = GroupChatsDAO()
        groupChats = dao.getAllGroupChats()
        result_map = []
        if not groupChats:
            return jsonify(Error="No group chats to show")
        else:
            for g in groupChats:
                result_map.append(self.build_groupChats_dict(g))
            return jsonify(GroupChats=result_map)

    def updateMessage(self, gid, uid, mid, json):
        dao = GroupChatsDAO()
        if not dao.getMessageById(gid, uid, mid):
            return jsonify(Error = "Message not found"), 404
        else:
            if len(json) != 6:
                return jsonify(Error="Malformed update request"), 400
            else:
                mmessage = json['mmessage']
                mupload_date = json['mupload_date']
                msize = json['msize']
                mlength = json['mlength']
                mtype = json['mtype']
                mpath = json['mpath']

                if mmessage and mupload_date and msize and mlength and mtype and mpath:
                    dao.updateMessage(gid, uid, mid, mmessage, mupload_date, msize, mlength, mtype, mpath)
                    result = self.build_message_attributes(mid, mmessage, mupload_date, msize, mlength, mtype, mpath)
                    return jsonify(Message =result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteMessage(self, gid, mid):
        dao = GroupChatsDAO()
        if not dao.getMessageById(gid, mid):
            return jsonify(Error="Message not found."), 404
        else:
            dao.deleteMessage(gid, mid)
            return jsonify(DeleteStatus="OK"), 200

    def addUserToGroupChat(self, userid, groupchatid, form):
        if len(form) != 4:
            return jsonify(Error="Malformed Post Request"), 400
        else:
            username = form['username']
            ucreation_date = form['ucreation_date']
            urecent_login = form['urecent_login']
            if username and ucreation_date and urecent_login:
                dao = GroupChatsDAO()
                dao.addUserToGroupChat(userid, groupchatid)
                result = self.build_user_attributes(userid, username, ucreation_date, urecent_login)
                if result is None:
                    return jsonify(Error="Unable to add user to group chat")
                else:
                    return jsonify(UserAdded=result)

            else:
                return jsonify(Error="Malformed Post Request"), 400

    def getMessageLikesByMessageId(self, messageid):
        dao = GroupChatsDAO()
        row = dao.getMessageLikesByMessageId(messageid)
        if not row:
            return jsonify(Error="No Likes found for this message"), 404
        else:
            likes = self.build_likes_dict(row)
            return jsonify(Reaction=likes)

    def getMessageDislikesByMessageId(self, messageid):
        dao = GroupChatsDAO()
        row = dao.getMessageDislikesByMessageId(messageid)
        if not row:
            return jsonify(Error="No Dislikes found for this message"), 404
        else:
            dislikes = self.build_dislikes_dict(row)
            return jsonify(Reaction=dislikes)

    def getMessageLikesInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid, messageid):
        dao = GroupChatsDAO()
        result = dao.getMessageLikesInGroupChatByUserIdAndGroupChatIdAndMessageId(userid, groupchatid, messageid)
        result_map = []
        if result is None:
            return jsonify(Error="Unable to get reactions")
        else:
            for r in result:
                result_map.append(self.build_reactions_dict(r))
            return jsonify(Reactions=result_map)

    def getMessageDislikesInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid, messageid):
        dao = GroupChatsDAO()
        result = dao.getMessageDislikesInGroupChatByUserIdAndGroupChatIdAndMessageId(userid, groupchatid, messageid)
        result_map = []
        if result is None:
            return jsonify(Error="Unable to get reactions")
        else:
            for r in result:
                result_map.append(self.build_reactions_dict(r))
            return jsonify(Reactions=result_map)

    def getOwnerOfGroupChatById(self, groupchatid):
        dao = GroupChatsDAO()
        row = dao.getOwnerOfGroupChatById(groupchatid)
        if not row:
            return jsonify(Error="Owner not found"), 404
        else:
            owner = self.build_user_dict(row)
            return jsonify(Owner=owner)

    def getGroupChatInfoById(self, groupchatid):
        dao = GroupChatsDAO()
        row = dao.getGroupChatInfoById(groupchatid)
        if not row:
            return jsonify(Error="Group chat not found"), 404
        else:
            groupchat = self.build_groupChats_dict(row)
            return jsonify(GroupChat=groupchat)
