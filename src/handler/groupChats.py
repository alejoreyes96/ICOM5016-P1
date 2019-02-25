from flask import jsonify
from dao.groupChats import GroupChatsDAO

class ChatHandler:


    def build_message_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['muserid'] = row[1]
        result['muploadDate'] = row[2]
        result['msize'] = row[3]
        result['mcontent'] = row[4]
        result['mgroupid'] = row[5]
        result['mreaction'] = row[6]
        return result

    def build_message_attributes(self, mid, muserid, muploadDate, msize, mcontent, mgroupid, mreaction):
        result = {}
        result['mid'] = mid
        result['muserid'] = muserid
        result['muploadDate'] = muploadDate
        result['msize'] = msize
        result['mcontent'] = mcontent
        result['mgroupid'] = mgroupid
        result['mreaction'] = mreaction
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

    def build_groupChat_attributes(self, gid, gname, gcreationDate, guserList, gmediaList, gowner):
        result = {}
        result['gid'] = gid
        result['gname'] = gname
        result['gcreationDate'] = gcreationDate
        result['guserList'] = guserList
        result['gmediaList'] = gmediaList
        result['gowner'] = gowner
        return result



    def getAllGroupChats(self, userid):
        dao = GroupChatsDAO()
        chats_list = dao.getAllGroupChats(userid)
        result_list = []
        for row in chats_list:
            result = self.build_groupChat_dict(row)
            result_list.append(result)

        return jsonify(GroupChats=result_list)


    def getGroupChatById(self, gid, uid):
        dao = GroupChatsDAO()
        row = dao.getGroupChatById(gid, uid)
        if not row:
            return jsonify(Error = "Chat Not Found"), 404
        else:
            chat = self.build_groupChat_dict(row)
            return jsonify(Chat = chat)

    def getAllMessages(self, gid, uid):
        dao = GroupChatsDAO()
        messages_list = dao.getAllMessages(gid, uid)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)

        return jsonify(Messages=result_list)

    def createMessageJson(self, groupChatId, userid, json):
            # gname = json['gname']
            # gcreationDate = json['gcreationDate']
            # guserList = json['guserList']
            # gmediaList = json['gmediaList']
            # gowner = json['gowner']
            muserid = userid
            muploadDate= "25/2/2019"
            msize = '250MB'
            mcontent = ['name: "Kingdom-hearts-3-tips-tricks-strategies-1.jpg"', 'type: "image/jpeg"']
            mgroupid = groupChatId
            mreaction = ['like: 50', 'dislike: 1']

            if muserid and muploadDate and msize and mcontent and mgroupid and mreaction:
                dao = GroupChatsDAO()
                mid = dao.insertMessage()
                result = self.build_message_attributes(mid, muserid, muploadDate, msize, mcontent, mgroupid, mreaction)
                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getMessageById(self, gid, uid, mid):
        dao = GroupChatsDAO()
        row = dao.getMessageById(gid, uid, mid)
        if not row:
            return jsonify(Error="Message Not Found"), 404
        else:
            message = self.build_message_dict(row)
            return jsonify(Message=message)


    def updateMessage(self, gid, userName, mid, form):
        dao = GroupChatsDAO()
        if not dao.getMessageById(gid, userName, mid):
            return jsonify(Error = "Message not found"), 404
        else:
            # if len(form) != 4:
            #     return jsonify(Error="Malformed update request"), 400
            # else:
                # gname = form['gname']
                # guserList = form['guserList']
                # gmediaList = form['gmediaList']
                # gowner = form['gowner']

                # if gname and guserList and gmediaList and gowner:
                    updated = dao.updateMessage(gid, userName, mid)
                    result = self.build_message_attributes(updated[0], updated[1], updated[2], updated[3], updated[4], updated[5], updated[6])
                    return jsonify(Message =result), 200
                # else:
                #     return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteMessage(self, gid, userName, mid):
        dao = GroupChatsDAO()
        if not dao.getMessageById(gid, userName, mid):
            return jsonify(Error="Group Chat not found."), 404
        else:
            dao.delete(mid)
            return jsonify(DeleteStatus="OK"), 200

    def likeMessage(self, gid, uid, mid):
        dao = GroupChatsDAO()
        if not dao.getMessageById(gid, uid, mid):
            return jsonify(Error="Message not found"), 404
        else:
            # if len(form) != 4:
            #     return jsonify(Error="Malformed update request"), 400
            # else:
            # gname = form['gname']
            # guserList = form['guserList']
            # gmediaList = form['gmediaList']
            # gowner = form['gowner']

            # if gname and guserList and gmediaList and gowner:
            updated = dao.likeMessage(gid, uid, mid)
            result = self.build_message_attributes(updated[0], updated[1], updated[2], updated[3], updated[4],
                                                   updated[5], updated[6])
            return jsonify(Message=result), 200
        # else:
        #     return jsonify(Error="Unexpected attributes in update request"), 400

    def dislikeMessage(self, gid, uid, mid):
        dao = GroupChatsDAO()
        if not dao.getMessageById(gid, uid, mid):
            return jsonify(Error="Message not found"), 404
        else:
            # if len(form) != 4:
            #     return jsonify(Error="Malformed update request"), 400
            # else:
            # gname = form['gname']
            # guserList = form['guserList']
            # gmediaList = form['gmediaList']
            # gowner = form['gowner']

            # if gname and guserList and gmediaList and gowner:
            updated = dao.dislikeMessage(gid, uid, mid)
            result = self.build_message_attributes(updated[0], updated[1], updated[2], updated[3], updated[4],
                                                   updated[5], updated[6])
            return jsonify(Message=result), 200
        # else:
        #     return jsonify(Error="Unexpected attributes in update request"), 400

    def createGroupChatJson(self, json):
            # gname = json['gname']
            # gcreationDate = json['gcreationDate']
            # guserList = json['guserList']
            # gmediaList = json['gmediaList']
            # gowner = json['gowner']
            gname = 'Chat1'
            gcreationDate = '25/2/19'
            guserList = ["Ale","Crys","Kahlil"]
            gmediaList = [1, 'Ale', "24/2/2019", "230MB", "sample_video.mp4", 1, ["likes: 450", "dislikes: 64"]]
            gowner = "Ale"

            if gname and gcreationDate and guserList and gmediaList and gowner:
                dao = GroupChatsDAO()
                gid = dao.insert(gname, gcreationDate, guserList, gmediaList, gowner)
                result = self.build_groupChat_attributes(gid, gname, gcreationDate, guserList, gmediaList, gowner)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateGroupChat(self, gid, userName, form):
        dao = GroupChatsDAO()
        if not dao.getGroupChatById(gid, userName):
            return jsonify(Error = "GroupChat not found"), 404
        else:
            # if len(form) != 4:
            #     return jsonify(Error="Malformed update request"), 400
            # else:
                # gname = form['gname']
                # guserList = form['guserList']
                # gmediaList = form['gmediaList']
                # gowner = form['gowner']

                # if gname and guserList and gmediaList and gowner:
                    updated = dao.update(gid, userName)
                    result = self.build_groupChat_attributes(updated[0], updated[1], updated[2], updated[3], updated[4], updated[5])
                    return jsonify(GroupChat=result), 200
                # else:
                #     return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteGroupChat(self, gid, userName):
        dao = GroupChatsDAO()
        if not dao.getGroupChatById(gid, userName):
            return jsonify(Error="Group Chat not found."), 404
        else:
            dao.delete(gid)
            return jsonify(DeleteStatus="OK"), 200