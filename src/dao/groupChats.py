from flask import jsonify
class GroupChatsDAO:

    def getAllGroupChats(self, uid):
        if uid == 'Ale':
            allGroups = [[1, "Test", "12/2/19", ["Ale", "Kahlil", "Crys"],
                          [[1, uid, "24/2/2019", "230MB", "sample_video.mp4", 1,["likes: 2500", "dislikes: 30"]],
                           [2, uid, "24/2/2019", "20MB", "sample_image.jpeg", 2, ["likes: 800", "dislikes: 80"]]], "Ale"],
                         [2, "Char2", "23/2/19", ["You", "Me", "Us"],
                          [[1, uid, "24/2/2019", "230MB", "sample_video.mp4", 1, ["likes: 14", "dislikes: 58"]],
                           [2, uid, "24/2/2019", "20MB", "sample_image.jpeg", 1, ["likes: 140", "dislikes: 51"]]], "Ale"]]
        elif uid == 'Kahlil':
            allGroups = [[1, "Chat1", "23/2/19", ["Ale", "Kahlil", "Crys"],
                          [[1, uid, "24/2/2019", "230MB", "sample_video.mp4", 1, ["likes: 875", "dislikes: 250"]],
                           [2, uid, "24/2/2019", "20MB", "sample_image.jpeg", 2, ["likes: 1051", "dislikes: 542"]]], "Kahlil"]]

        elif uid == 'Crystal':
            allGroups = [[1, "Chat1", "24/2/19", ["Ale", "Kahlil", "Crys"],
                          [[1, uid, "24/2/2019", "230MB", "sample_video.mp4", 1, ["likes: 450", "dislikes: 64"]],
                           [2, uid, "24/2/2019", "20MB", "sample_image.jpeg", 2, ["likes: 45", "dislikes: 7"]]], "Crystal"]]
        else:
            allGroups = []
        return allGroups

    def getGroupChatById(self, gid, uid):
        allGroups = self.getAllGroupChats(uid)
        result = []
        for i in allGroups:
            for j in i:
                if i[0] == gid:
                    result = i
        return result

    def getAllMessages(self, gid, uid):
        group = self.getGroupChatById(gid,uid)
        message = group[4]
        return message

    def getMessageById(self, gid, uid, mid):
        result = self.getAllMessages(gid, uid)
        message = []
        for i in result:
            if i[0] == mid:
                message = i
        return message

    def update(self, gid, userName):
        result = self.getGroupChatById(gid, userName)
        result[2] = 'UpdatedUser'

        return result

    def delete(self, gid):
        return gid

    def insert(self, gname, gcreationDate, guserList, gmediaList, gowner):
        gid = 4
        return gid

    def insertMessage(self):
        mid = 3
        return mid

    def updateMessage(self, gid, userName, mid):
        result = self.getMessageById(gid,userName, mid)
        result[2] = 'updated: 26/2/2019'
        return result

    def likeMessage(self, gid, uid, mid):
        result = self.getMessageById(gid,uid, mid)
        result[2] = 'updateLikes: 26/2/2019'
        return result

    def dislikeMessage(self, gid, uid, mid):
        result = self.getMessageById(gid,uid, mid)
        result[2] = 'updateDislikes: 26/2/2019'
        return result
