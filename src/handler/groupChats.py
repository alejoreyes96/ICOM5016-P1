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

    def createGroupChat(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            gname = form['gname']
            gcreationDate = form['gcreationDate']
            guserList = form['guserList']
            gmediaList = form['gmediaList']
            gowner = form['gowner']
            if gname and gcreationDate and guserList and gmediaList and gowner:
                dao = GroupChatsDAO()
                gid = dao.insert(gname, gcreationDate, guserList, gmediaList, gowner)
                result = self.build_groupChat_attributes(gid, gname, gcreationDate, guserList, gmediaList, gowner)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateGroupChat(self, gid, form):
        dao = GroupChatsDAO()
        if not dao.getGroupChatById(gid):
            return jsonify(Error = "GroupChat not found"), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                gname = form['gname']
                guserList = form['guserList']
                gmediaList = form['gmediaList']
                gowner = form['gowner']
                if gname and guserList and gmediaList and gowner:
                    dao.update(gid, gname, guserList, gmediaList, gowner)
                    result = self.build_groupChat_attributes(gid, gname, guserList, gmediaList, gowner)
                    return jsonify(GroupChat=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteGroupChat(self, gid):
        dao = GroupChatsDAO()
        if not dao.getGroupChatById(gid):
            return jsonify(Error="Group Chat not found."), 404
        else:
            dao.delete(gid)
            return jsonify(DeleteStatus="OK"), 200