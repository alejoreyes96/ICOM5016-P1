from flask import jsonify
class GroupChatsDAO:

    def getAllGroupChats(self, userid):
        if userid == 'Ale':
            result = [[1, "Test", "12/2/19", ["Ale","Kahlil", "Crys"], ["media1", "media2", "media3"], "Ale"], [2, "Char2", "23/2/19", ["You", "Me", "Us"], "media1", "Ale"]]
        elif userid == 'Kahlil':
            result = [[1, "Chat1", "23/2/19", ["Ale", "Kahlil", "Crys"], ["media1", "video"], "Kahlil"]]
        elif userid == 'Crystal':
            result = [[1, "Chat1", "24/2/19", ["Ale", "Kahlil", "Crys"], ["media1", "video4"], "Crystal"]]
        else:
            result = []
        return result

    def getGroupChatById(self, gid):
        allGroups = [[1, "App", "12/2/19", ["Ale","Kahlil", "Crys"], ["media1", "media2", "media3"], "Ale"], [2, "App", "23/2/19", ["You", "Me", "Us"], "media1", "Ale"]]
        result = []
        for i in allGroups:
            for j in i:
                if i[0] == gid:
                    result = i
        return result

    def update(self, gid, gname, guserList, gmediaList, gowner):
        return gid

    def delete(self, gid):
        return gid

    def insert(self, gname, gcreationDate, guserList, gmediaList, gowner):
        gid = 0;
        return gid
