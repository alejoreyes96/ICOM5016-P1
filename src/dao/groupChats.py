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

    def update(self, gid, gname, guserList, gmediaList, gowner):
        return gid

    def delete(self, gid):
        return gid

    def insert(self, gname, gcreationDate, guserList, gmediaList, gowner):
        gid = 0;
        return gid
