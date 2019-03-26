from config.dbconfig import pg_config
import psycopg2

class GroupChatsDAO:

    # def init(self):
    connection_url = "user=%s password=%s host=%s port=%s dbname=%s" % (
    pg_config['user'], pg_config['password'], pg_config['host'],
    pg_config["port"], pg_config["dbname"])
    conn = psycopg2.connect(connection_url)

    def getAvailableGroupChatsByUserId(self, userid):
        cursor = self.conn.cursor()
        query = 'select gid, gname, gcreation_date, gpicture_id_path, first_name,last_name,users.uid from groupchats \
          natural inner join ismember natural inner join users inner join Human on human.huid=users.human_id where uid = %s;'
        cursor.execute(query, (userid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllGroupChats(self):
        cursor = self.conn.cursor()
        query = 'select gid, gname,gcreation_date,gpicture_id_path,first_name,last_name,uid from groupChats \
        inner join human on groupChats.huid=human.huid inner join users on users.human_id=human.huid;'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatById(self, gid):
        cursor = self.conn.cursor()
        query = 'select first_name, last_name, gid, gname,gcreation_date,gpicture_id_path, uid \
                from human natural inner join groupchats inner join users on human.huid=users.human_id \
                    where gid = ANY(select gid from groupchats inner join Human on \
                    groupChats.huid=human.huid inner join users on users.human_id=human.huid where gid=%s);'
        cursor.execute(query, (gid,))
        result = []
        result = cursor.fetchone()
        return result

    def updateGroupChat(self, gid, gname, gpicture_id):
        result = '4/1/19'
        return result

    def deleteGroupChat(self, gid):
        result = []
        return result

    def createGroupChat(self, userid, gname):
        if (userid == 1 or userid == 2 or userid == 3) and gname == 'Creators':
            return [1, '3/1/19']
        elif userid == 1:
            return [4, '3/1/19']
        elif (userid == 2 or userid == 3) and gname == 'Bros':
            return [3, '3/1/19']
        else:
            return [5, '3/1/19']

        return result

    def addUserToGroupChat(self, uid, groupchatid):
        result = []
        if uid == 1:
            result = [1, 'crystal.torres', '02/25/2019', '03/26/2019']
        elif uid == 2:
            result = [2, 'kahlil-14', '02/25/2019', '03/28/2019']
        elif uid == 3:
            result = [3, 'alejo', '02/25/2019', '02/27/2019']
        return result

    def deleteGroupChatById(self, userid, groupchatid):
        result = []
        return result

    def deleteUserFromGroupChat(self, userid, userid2, groupchatid):
        result = []
        return result

    def getMessagesByHashtagStringInGroupChat(self, userid, groupchatid, hashtagstring):
        cursor = self.conn.cursor()
        query = "select mid,mmessage,mupload_date,msize,mlength,mtype,mmedia_path,hhashtag from users natural \
                        inner join messages natural inner join contains natural inner join hashtags natural inner join \
                        posted_to where gid = %s and hhashtag=%s;"
        cursor.execute(query, (groupchatid, hashtagstring,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesFromGroupChatByUserIdAndGroupChatId(self, userid, groupchatid):
        cursor = self.conn.cursor()
        query = "select mid,mmessage,mupload_date,msize,mlength,mtype,mmedia_path,uid from users natural \
                inner join messages natural inner join posted_to where gid = %s Order By messages.mid;"
        cursor.execute(query, (groupchatid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageLikesByMessageId(self, messageid):
        cursor = self.conn.cursor()
        query = "select messages.mid, count(*) from messages inner join reactions on reactions.mid=messages.mid \
        where messages.mid=%s and rtype=True Group By messages.mid;"
        cursor.execute(query, (messageid,))
        result = cursor.fetchone()
        return result

    def getMessageDislikesByMessageId(self, messageid):
        cursor = self.conn.cursor()
        query = "select messages.mid, count(*) from messages inner join reactions on reactions.mid=messages.mid \
        where messages.mid=%s and rtype=False Group By messages.mid;"
        cursor.execute(query, (messageid,))
        result = cursor.fetchone()
        return result

    def replyToMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid, messageid, text):
        result = []
        return result

    def insertMessage(self, uid, gid, mmessage, mupload_date, msize, mlength, mtype, mpath, mhashtag):
        result = []
        mid = 1
        return mid

    def getMessageFromGroupChatById(self, uid, gid, mid):
        cursor = self.conn.cursor()
        query = "select messages.mid,mmessage,mupload_date,msize,mlength,mtype,mmedia_path,messages.uid\
         from users natural inner join messages natural inner join posted_to where posted_to.gid=%s\
        and messages.mid=%s Order by messages.mid;"
        cursor.execute(query, (gid, mid,))
        result = cursor.fetchone()
        return result



    def getReplyById(self, uid, gid, mid, rpid):
        cursor = self.conn.cursor()
        query = "select replies.rpid,rpreply,rpupload_date,hhashtag from messages natural inner join contains \
            inner join replies on contains.rpid=replies.rpid inner join posted_to on posted_to.mid=messages.mid inner \
            join hashtags on contains.hid=hashtags.hid where messages.mid=%s and replies.rpid=%s and posted_to.gid=%s;"
        cursor.execute(query, (mid, rpid, gid,))
        result = cursor.fetchone()
        return result

    def getMessageReactionsInGroupChatByUserIdAndGroupChatIdAndMessageId(self, uid, groupchatid, messageid):
        cursor = self.conn.cursor()
        query = "select reactions.rtype, reactions.rid, users.uid, user_name, rupload_date, human.first_name, \
        human.last_name from messages inner join users on users.uid=messages.uid  inner join reactions on \
        reactions.mid=messages.mid inner join ismember on users.uid=ismember.uid inner join human on \
        users.human_id=human.huid where messages.mid=%s and ismember.gid=%s;"
        cursor.execute(query, (messageid, groupchatid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageLikesInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid, messageid):
        cursor = self.conn.cursor()
        query = "select reactions.rtype, reactions.rid, users.uid, user_name, rupload_date, human.first_name, \
                human.last_name from messages inner join users on users.uid=messages.uid  inner join reactions on \
                reactions.mid=messages.mid inner join ismember on users.uid=ismember.uid inner join human on \
                users.human_id=human.huid where messages.mid=%s and ismember.gid=%s and reactions.rtype=true;"
        cursor.execute(query, (messageid, groupchatid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageDislikesInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid, messageid):
        cursor = self.conn.cursor()
        query = "select reactions.rtype, reactions.rid, users.uid, user_name, rupload_date, human.first_name, \
                human.last_name from messages inner join users on users.uid=messages.uid  inner join reactions on \
                reactions.mid=messages.mid inner join ismember on users.uid=ismember.uid inner join human on \
                users.human_id=human.huid where messages.mid=%s and ismember.gid=%s and reactions.rtype=false;"
        cursor.execute(query, (messageid, groupchatid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select messages.mid,mmessage,mupload_date,msize,mlength,mtype,mmedia_path, uid\
                 from messages;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatInfoById(self, groupchatid):
        cursor = self.conn.cursor()
        query = 'select gid, gname,gcreation_date,gpicture_id_path,first_name,last_name,uid from groupChats \
                inner join Human on groupChats.huid=human.huid inner join users on users.human_id=human.huid\
                where groupChats.gid=%s;'
        cursor.execute(query, (groupchatid,))
        result = cursor.fetchone()
        return result

    def getOwnerOfGroupChatById(self, groupchatid):
        cursor = self.conn.cursor()
        query = 'select users.uid, user_name, ucreation_date, umost_recent_login, first_name,last_name\
        from groupChats inner join Human on groupChats.huid=human.huid inner join users on \
        users.human_id=human.huid where groupChats.gid=%s;'
        cursor.execute(query, (groupchatid,))
        result = cursor.fetchone()
        return result

    # def getRepliesFromMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid, messageid):

    def updateReply(self, uid, gid, mid, rid, rpreply, rpupload_date, rphashtag):
        result = []
        return result

    def deleteReply(self, uid, gid, mid, rid):
        result = []
        return result

    def updateMessage(self, uid, gid, mid, mmessage, mupload_date, msize, mlength, mtype, mpath):
        result = []
