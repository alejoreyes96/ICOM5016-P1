from flask import jsonify
from dao.groupChats import GroupChatsDAO
from dao.statistics import StatsDAO
from dao.user import UserDAO
import datetime as dt

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
        result['mhashtag'] = row[7]
        result['uid'] = row[8]
        return result

    def build_messages_per_day(self, row):
        result = {}
        result['day'] = row[0]
        result['total'] = row[1]
        return result

    def build_message_attributes(self, mid, mmessage, mupload_date, msize, mlength, mgif, mpath, mhashtag):
        result = {}
        result['mid'] = mid
        result['mmessage'] = mmessage
        result['mupload_date'] = mupload_date
        result['msize'] = msize
        result['mlength'] = mlength
        result['mgif'] = mgif
        result['mpath'] = mpath
        result['mhashtag'] = mhashtag

        return result

    def build_groupChat_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['gcreation_date'] = row[2]
        result['gpicture_id'] = row[3]
        result['gowner_id'] = row[4]
        return result

    def build_groupChat_attributes(self, gid, gname, gcreation_date, gpicture_id,userid):
        result = {}
        result['gid'] = gid
        result['gname'] = gname
        result['gcreation_date'] = gcreation_date
        result['gpicture_id'] = gpicture_id
        result['gowner_id'] = userid
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
    def build_ismember_dict(self, row):
         result = {}
         result['gid'] = row[0]
         result['uid'] = row[1]
         return result

    def build_ismember_attributes(self,gid,uid):
        result = {}
        result['gid'] = gid
        result['uid'] = uid
        return result

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
        result['first_name']=row[5]
        result['last_name']=row[6]
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
        result['rp_reply_text'] = row[1]
        result['rpupload_date'] = row[2]
        result['uid'] = row[3]
        result['user_name'] = row[4]
        result['first_name'] = row[5]

        return result

    def build_reply_attributes(self, rpid, rp_reply_text, rpupload_date, mid, uid):
        result = {}
        result['rpid'] = rpid
        result['rpupload_date'] = rpupload_date
        result['rp_reply_text'] = rp_reply_text
        result['mid'] = mid
        result['uid'] = uid
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

    def build_user_attributes(self, uid, uname, ucreationDate, urecentLogin):
        result = {}
        result['uid'] = uid
        result['uname'] = uname
        result['ucreationDate'] = ucreationDate
        result['urecentLogin'] = urecentLogin
        return result

    def build_likes_dict(self, row):
        result = {}
        result['likes'] = row[0]
        return result

    def build_dislikes_dict(self, row):
        result = {}
        result['dislikes'] = row[0]
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
            gcreation_date = dt.datetime.now().date().strftime("%m/%d/%Y")
            if gname and gpicture_id and userid:
                dao = GroupChatsDAO()
                gid= dao.createGroupChat(userid, gname,gpicture_id)
                result = self.build_groupChat_attributes(gid, gname, gcreation_date, gpicture_id,userid)
                if result is None:
                    return jsonify(Error="Unable to create group chat")
                else:
                    return jsonify(GroupChat=result)

            else:
                return jsonify(Error="Malformed Post Request"), 400

    def getGroupChatById(self, gid):
        dao = GroupChatsDAO()
        chat_list = dao.getGroupChatById(gid)
        result_map = []
        if not chat_list:
            return jsonify(Error="Message Not Found"), 404
        else:
            for row in chat_list:
                result = self.build_groupChats_dict(row)
                result_map.append(result)
        return jsonify(GroupChat=result_map), 201

    def updateGroupChat(self, gid, form):
         dao = GroupChatsDAO()
         if not dao.getGroupChatById(gid):
             return jsonify(Error="GroupChat not found"), 404
         else:
             if len(json) != 2:
                 return jsonify(Error="Malformed update request"), 400
             else:
                gname = json['gname']
                gpicture_id = json['gpicture_id']
                gcreation_date = dt.datetime.now().date().strftime("%m/%d/%Y")
                if gname and gpicture_id:
                     gid = dao.updateGroupChat(gid, gname, gpicture_id)
                     result = self.build_groupChat_attributes(gid, gname,gcreation_date,gpicture_id)
                     return jsonify(GroupChat=result), 200
                else:
                     return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteGroupChatById(self, gid,uid):
        dao = GroupChatsDAO()
        if not dao.getGroupChatByGroupChatIdAndUserId(gid,uid):
            return jsonify(Error="Group Chat not found."), 404
        else:
            dao.deleteGroupChatById(gid)
            return jsonify(DeleteStatus="OK"), 200

    def deleteGroupChatByName(self, gname):
        dao = GroupChatsDAO()
        if not dao.getGroupChatByName(gname):
            return jsonify(Error="Group Chat not found."), 404
        else:
            dao.deleteGroupChatByName(gname)
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

    def getRepliesFromMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(self,userid, groupchatid, messageid):
        dao = GroupChatsDAO()
        result = dao.getRepliesFromMessageInGroupChatByUserIdAndGroupChatIdandMessageId(userid, groupchatid, messageid)
        result_map = []
        if result is None:
            return jsonify(Error="Unable to get replies")
        else:
            for r in result:
                result_map.append(self.build_reply_dict(r))
            return jsonify(Replies=result_map)


    def getMessageLikesInGroupChatByUserIdGroupChatIdAndMessageId(self,messageid,groupchatid):
        dao = GroupChatsDAO()
        result = dao.getMessageLikesInGroupChatByUserIdGroupChatIdAndMessageId(groupchatid, messageid)
        result_map = []
        if result is None:
            return jsonify(Error="Unable to get reactions")
        else:
            for r in result:
                result_map.append(self.build_reactions_dict(r))
            return jsonify(Reactions=result_map)

    def getMessageFromGroupChatById(self, gid, uid, mid):
        dao = GroupChatsDAO()
        row = dao.getMessageFromGroupChatById(gid, uid, mid)
        if not row:
            return jsonify(Error="Message Not Found"), 404
        else:
            message = self.build_message_dict(row)
            return jsonify(Message=message)

    def getMessageDislikesInGroupChatByUserIdGroupChatIdAndMessageId(self,userid,messageid,groupchatid):
        dao = GroupChatsDAO()
        result = dao.getMessageDislikesInGroupChatByUserIdGroupChatIdAndMessageId(userid,groupchatid, messageid)
        result_map = []
        if result is None:
            return jsonify(Error="Unable to get reactions")
        else:
            for r in result:
                result_map.append(self.build_reactions_dict(r))
            return jsonify(Reactions=result_map)

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

    def getGroupChatInfoById(self, groupchatid):
        dao = GroupChatsDAO()
        row = dao.getGroupChatInfoById(groupchatid)
        if not row:
            return jsonify(Error="Group chat not found"), 404
        else:
            groupchat = self.build_groupChats_dict(row)
            return jsonify(GroupChat=groupchat)

    def getMessagesPerDay(self):
        dao = StatsDAO()
        messagesperday = dao.getMessagesPerDay()
        result_map = []
        if not messagesperday:
            return jsonify(Error="No messages")
        else:
            for m in messagesperday:
                result_map.append(self.build_messages_per_day(m))
            return jsonify(List=result_map)



    def reactToMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(self,userid,groupchatid,messageid,form):
        dao = GroupChatsDAO()
        if len(form) != 1:
            return jsonify(Error="Malformed update request"), 400
        else:
            rtype = json['rtype']
            rupload_date = dt.datetime.now().date().strftime("%m/%d/%Y")
            if rtype and rupload_date:
                rid = dao.reactToMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(userid,groupchatid,messageid,rtype)
                result = self.build_reactions_attributes(rid,rtype,rupload_date)
                return jsonify(Reaction=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def replyToMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid, messageid, json):
        dao = GroupChatsDAO()
        if len(json) != 2:
            return jsonify(Error="Malformed update request"), 400
        else:
            rpreply = json['rpreply']
            rpupload_date = dt.datetime.now().date().strftime("%m/%d/%Y")
            if rtype and rpupload_date:
                rpid = dao.replyToMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(userid,groupchatid,messageid,rpreply)
                result = self.build_reply_attributes(rpid,rpupload_date,rpreply,messageid,userid)
                return jsonify(Reaction=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def addUserToGroupChat(self,json):
        dao = GroupChatsDAO()
        if len(json) != 2:
            return jsonify(Error="Malformed update request"), 400
        else:
            userid = json['uid']
            groupchatid = json['gid']
            if email:
                gid = dao.addUserToGroupChat(userid, groupchatid)
                result = self.build_ismember_attributes(gid,userid)
                return jsonify(Reaction=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertMessage(self, userid, groupchatid,json):
        dao = GroupChatsDAO()
        if len(json) != 7:
            return jsonify(Error="Malformed update request"), 400
        else:

            if rtype and rupload_date:
                rid = dao.addReaction(userid, groupchatid, messageid, rtype, rupload_date)
                result = self.build_reactions_attributes(rid, rtype, rupload_date)
                return jsonify(Reaction=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def reactToReplyInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid, messageid, json):
        dao = GroupChatsDAO()
        if len(form) != 1:
            return jsonify(Error="Malformed update request"), 400
        else:
            rtype = json['rtype']
            rupload_date = dt.datetime.now().date().strftime("%m/%d/%Y")
            if rtype:
                rid = dao.reactToReplyInGroupChatByUserIdAndGroupChatIdAndMessageId(userid, groupchatid, messageid,rtype)
                result = self.build_reactions_attributes(rid, rtype, rupload_date)
                return jsonify(Reaction=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteMessage(self, mid):
        dao = GroupChatsDAO()
        if not dao.getMessageById(mid):
            return jsonify(Error="Group Chat not found."), 404
        else:
            dao.deleteGroupChatByName(gname)
            return jsonify(DeleteStatus="OK"), 200


    def deleteReply(self, rpid):
        dao = GroupChatsDAO()
        if not dao.getReplyById(rpid):
            return jsonify(Error="Group Chat not found."), 404
        else:
            dao.deleteReply(rpid)
            return jsonify(DeleteStatus="OK"), 200

    def deleteReaction(self, rid):
        dao = GroupChatsDAO()
        if not dao.getReactionById(rid):
            return jsonify(Error="Group Chat not found."), 404
        else:
            dao.deleteReaction(rid)
            return jsonify(DeleteStatus="OK"), 200

    def deleteUserFromGroupChat(self, gid,userid):
        dao = GroupChatsDAO()
        if not dao.getMemberFromGroupChat(gid,userid):
            return jsonify(Error="Group Chat not found."), 404
        else:
            dao.deleteUserFromGroupChat(userid,gid)
            return jsonify(DeleteStatus="OK"), 200

    def updateMessage(self, gid, form):
        dao = GroupChatsDAO()
        if not dao.getGroupChatById(gid):
            return jsonify(Error="GroupChat not found"), 404
        else:
            if len(json) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                gname = json['gname']
                gpicture_id = json['gpicture_id']
                gcreation_date = dt.datetime.now().date().strftime("%m/%d/%Y")
                if gname and gpicture_id:
                    gid = dao.updateGroupChat(gid, gname, gpicture_id)
                    result = self.build_groupChat_attributes(gid, gname, gcreation_date, gpicture_id)
                    return jsonify(GroupChat=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def updateReply(self, gid, form):
        dao = GroupChatsDAO()
        if not dao.getGroupChatById(gid):
            return jsonify(Error="GroupChat not found"), 404
        else:
            if len(json) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                gname = json['gname']
                gpicture_id = json['gpicture_id']
                gcreation_date = dt.datetime.now().date().strftime("%m/%d/%Y")
                if gname and gpicture_id:
                    gid = dao.updateGroupChat(gid, gname, gpicture_id)
                    result = self.build_groupChat_attributes(gid, gname, gcreation_date, gpicture_id)
                    return jsonify(GroupChat=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def updateReaction(self, gid, form):
        dao = GroupChatsDAO()
        if not dao.getGroupChatById(gid):
            return jsonify(Error="GroupChat not found"), 404
        else:
            if len(json) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                gname = json['gname']
                gpicture_id = json['gpicture_id']
                gcreation_date = dt.datetime.now().date().strftime("%m/%d/%Y")
                if gname and gpicture_id:
                    gid = dao.updateGroupChat(gid, gname, gpicture_id)
                    result = self.build_groupChat_attributes(gid, gname, gcreation_date, gpicture_id)
                    return jsonify(GroupChat=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400