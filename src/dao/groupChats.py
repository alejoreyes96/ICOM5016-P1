#from config.dbconfig import pg_config
import psycopg2
import datetime as dt

class GroupChatsDAO:

    # def __init__(self):
    # connection_url = "user=%s password=%s host=%s port=%s dbname=%s" % (pg_config['user'], pg_config['password'],\
    # pg_config['host'],pg_config["port"], pg_config["dbname"])
    # conn = psycopg2.connect(connection_url)

    def getAvailableGroupChatsByUserId(self, userid):
        cursor = self.conn.cursor()
        query = 'select  gid, gname, gcreation_date, gpicture_id_path, first_name,last_name,uid from group_chats\
         natural inner join ismember natural inner join users inner join Human on human.huid=human_id where \
         users.uid = %s;'
        cursor.execute(query, (userid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatInfoById(self,groupchatid):
        cursor = self.conn.cursor()
        query = 'select gid, gname,gcreation_date,gpicture_id_path,first_name,last_name,uid from group_Chats \
                inner join Human on group_Chats.huid=human.huid inner join users on users.human_id=human.huid\
                where group_Chats.gid=%s;'
        cursor.execute(query,(groupchatid,))
        result = cursor.fetchone()
        return result

    def getAllGroupChats(self):
        cursor = self.conn.cursor()
        query = 'select gid, gname,gcreation_date,gpicture_id_path,first_name,last_name,uid from group_Chats \
        inner join Human on group_Chats.huid=human.huid inner join users on users.human_id=human.huid;'
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getGroupChatById(self, gid):
        cursor = self.conn.cursor()
        query = "select gid, gname, gcreation_date, gpicture_id_path, first_name,last_name,uid \
                 from group_chats inner join Human on group_Chats.huid=human.huid inner join users on \
                 users.human_id=human.huid where gid = %s;"
        cursor.execute(query, (gid,))
        result = cursor.fetchone()
        return result

    def getGroupChatByName(self, gname):
        cursor = self.conn.cursor()
        query = "select gid, gname, gcreation_date, gpicture_id_path, first_name,last_name,uid \
                 from group_chats inner join Human on group_Chats.huid=human.huid inner join users on \
                 users.human_id=human.huid where gname = %s;"
        cursor.execute(query, (gname,))
        result = cursor.fetchone()
        return result

    def getMessagesByHashtagStringInGroupChat(self, userid, groupchatid, hashtagstring):
        cursor = self.conn.cursor()
        query = "select messages.mid,mmessage,mupload_date,msize,mlength,mtype,mmedia_path,users.uid \
        from users inner join messages on messages.uid=users.uid inner join posted_to on messages.mid=posted_to.mid\
         inner join contains on contains.mid=messages.mid inner join hashtags on contains.hid=hashtags.hid \
         where gid=%s and hhashtag=%s;"
        cursor.execute(query, (groupchatid, hashtagstring,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesFromGroupChatByUserIdAndGroupChatId(self, userid, groupchatid):
        cursor = self.conn.cursor()
        query = "select mid,mmessage,mupload_date,msize,mlength,mtype,mmedia_path,uid from users natural \
                inner join messages natural inner join posted_to where gid = %s order by messages.mid;"
        cursor.execute(query, (groupchatid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageLikesByMessageId(self, messageid):
        cursor = self.conn.cursor()
        query = "select count(*), messages.mid from messages inner join reactions on reactions.mid=messages.mid  \
                where messages.mid=%s and rtype=True group by messages.mid;"
        cursor.execute(query, (messageid,))
        result = cursor.fetchone()
        return result

    def getMessageDislikesByMessageId(self, messageid):
        cursor = self.conn.cursor()
        query = "select count(*),messages.mid from messages inner join reactions on reactions.mid=messages.mid \
        where messages.mid=%s and rtype=False group by messages.mid;"
        cursor.execute(query, (messageid,))
        result = cursor.fetchone()
        return result


    def getMessageFromGroupChatById(self, uid, gid, mid):
        cursor = self.conn.cursor()
        query = "select messages.mid,mmessage,mupload_date,msize,mlength,mtype,mmedia_path,messages.uid\
         from users natural inner join messages natural inner join posted_to where posted_to.gid=%s\
        and messages.mid=%s;"
        cursor.execute(query, (gid, mid,))
        result = cursor.fetchone()
        return result


    def getReplyById(self, uid, gid, mid, rpid):
        cursor = self.conn.cursor()
        query = "select replies.rpid,rpreply,rpupload_date,rpsize,rplength,rppicture,rptype from messages\
        inner join replies on messages.mid=replies.mid inner join posted_to on posted_to.mid=messages.mid \
         where messages.mid=%s and posted_to.gid=%s and replies.rpid=%s;"
        cursor.execute(query, (mid,gid,rpid,))
        result = cursor.fetchone()
        return result

    def getRepliesFromMessageInGroupChatByUserIdAndGroupChatIdandMessageId(self, uid, gid, mid):
        cursor = self.conn.cursor()
        query = "select distinct replies.rpid,rpreply,rpupload_date,rpsize,rplength,rppicture,rptype,\
        users.uid, user_name, human.first_name from messages inner join replies on messages.mid=replies.mid \
        inner join users on users.uid=replies.uid inner join ismember on users.uid=ismember.uid inner join \
        human on users.human_id=human.huid inner join posted_to on posted_to.mid=messages.mid where \
        messages.mid=%s and posted_to.gid=%s;"
        cursor.execute(query, (mid,gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageReactionsInGroupChatByUserIdAndGroupChatIdAndMessageId(self,groupchatid, messageid):
        cursor = self.conn.cursor()
        query = "select reactions.rtype, reactions.rid, users.uid, user_name, rupload_date, human.first_name, \
        human.last_name from messages inner join reactions on \
        reactions.mid=messages.mid inner join users on users.uid=reactions.uid   inner join ismember on users.uid=ismember.uid inner join human on \
        users.human_id=human.huid  where messages.mid=%s and ismember.gid=%s;"
        cursor.execute(query, (groupchatid, messageid,))
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

    def getMessageLikesInGroupChatByUserIdGroupChatIdAndMessageId(self,messageid,groupchatid):
        cursor = self.conn.cursor()
        query = "select reactions.rtype, reactions.rid, users.uid, user_name, rupload_date, human.first_name, \
        human.last_name from messages inner join reactions on \
        reactions.mid=messages.mid inner join users on users.uid=reactions.uid   inner join ismember on users.uid=ismember.uid inner join human on \
        users.human_id=human.huid  where messages.mid=%s and ismember.gid=%s and reactions.rtype=true;"
        cursor.execute(query,(messageid,groupchatid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageDislikesInGroupChatByUserIdGroupChatIdAndMessageId(self,userid,messageid,groupchatid):
        cursor = self.conn.cursor()
        query = "select reactions.rtype, reactions.rid, users.uid, user_name, rupload_date, human.first_name, \
        human.last_name from messages inner join reactions on \
        reactions.mid=messages.mid inner join users on users.uid=reactions.uid   inner join ismember on users.uid=ismember.uid inner join human on \
        users.human_id=human.huid  where messages.mid=%s and ismember.gid=%s and reactions.rtype=false;"
        cursor.execute(query,(messageid,groupchatid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatByGroupChatIdAndUserId(self, gid,uid):
        cursor = self.conn.cursor()
        query = "select gid from group_chats inner join Human on group_Chats.huid=human.huid inner join users on \
                 users.human_id=human.huid where gid =%s and users.uid=%s;"
        cursor.execute(query, (gid,uid,))
        result = cursor.fetchone()
        return result

    def getMemberFromGroupChat(self,gid, userid):
        cursor = self.conn.cursor()
        query = "select * from ismember where gid=%s and uid=%s;"
        cursor.execute(query, (gid, userid,))
        result = cursor.fetchone()
        return result

    def getReplyByIdOnly(self,rpid):
        cursor = self.conn.cursor()
        query = "select * from replies where rpid=%s;"
        cursor.execute(query, (rpid,))
        result = cursor.fetchone()
        return result

    def getHashtagByHashtag(self, hhashtag):
        cursor = self.conn.cursor()
        query = "select * from hashtags where hhashtag=%s;"
        cursor.execute(query, (hhashtag,))
        result = cursor.fetchone()
        return result


    def getReactionByIdOnly(self, rid):
        cursor = self.conn.cursor()
        query = "select * from reactions where rid=%s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def replyToMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid,groupchatid,messageid,
                                                                    text,rpsize,rplength,rptype,rppath):
        cursor = self.conn.cursor()
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        query = "insert into replies(rpuload_date,rpreply,mid,uid,rppicture,rptype,rpsize,rplength) \
        values (%s, %s, %s, %s,%s,%s,%s,%s) returning rpid;"
        cursor.execute(query, (date,text,messageid,userid,rppath,rptype,rpsize,rplength,))
        rpid = cursor.fetchone()[0]
        self.conn.commit()
        return rpid

    def reactToReplyInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid,replyid,rtype):
        cursor = self.conn.cursor()
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        query = "insert into reactions(rupload_date,rtype,mid,rpid,uid) values(%s,%s,null,%s,%s) returning rid;"
        cursor.execute(query, (date,rtype,replyid,userid,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def reactToMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(self, userid, groupchatid, messageid,rtype):
        cursor = self.conn.cursor()
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        query = "insert into reactions(rupload_date,rtype,mid,rpid,uid) values(%s,%s,%s,null,%s) returning rid;"
        cursor.execute(query, (date,rtype,messageid,userid,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def insertMessage(self, uid, gid, mmessage, msize, mlength, mtype, mpath):
        cursor = self.conn.cursor()
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        query = "with first_get as(insert into messages(uid,mupload_date,msize,mmessage,mmedia_path,mlength,mtype)\
        values(%s,%s,%s,%s,%s,%s,%s) returning mid)\
        insert into posted_to(mid,gid) values((select mid from first_get),%s) returning mid;"
        cursor.execute(query, (uid, date, msize, mmessage, mpath,mlength, mtype,gid,))
        mid = cursor.fetchone()[0]
        self.conn.commit()
        return mid

    def insertHashtagAndContainsFromMessage(self,mid,hhashtag):
        cursor = self.conn.cursor()
        query = "with first_try as (insert into hashtags(hhashtag) values(%s) returning hid) insert into \
        contains(mid,hid,rpid) values(%s,(select hid from first_try),null) returning cid;"
        cursor.execute(query, (hhashtag,mid,))
        hid = cursor.fetchone()[0]
        self.conn.commit()
        return hid

    def insertContainsFromMessage(self,mid,hhashtag):
        cursor = self.conn.cursor()
        query = "with first_try as (select hid from hashtags where hhashtag=%s)insert into contains(mid,hid,rpid)\
        values(%s,(select hid from first_try),null) returning cid;"
        cursor.execute(query, (hhashtag,mid,))
        hid = cursor.fetchone()[0]
        self.conn.commit()
        return hid

    def insertHashtagAndContainsFromReply(self,rpid,hhashtag):
        cursor = self.conn.cursor()
        query = "with first_try as (insert into hashtags(hhashtag) values(%s) returning hid) insert into \
        contains(mid,hid,rpid) values(null,(select hid from first_try),%s) returning cid;"
        cursor.execute(query, (hhashtag,rpid,))
        hid = cursor.fetchone()[0]
        self.conn.commit()
        return hid

    def insertContainsFromReply(self, rpid, hhashtag):
        cursor = self.conn.cursor()
        query = "with first_try as (select hid from hashtags where hhashtag=%s)insert into contains(mid,hid,rpid)\
           values(null,(select hid from first_try),%s) returning cid;"
        cursor.execute(query, (hhashtag, mid,))
        hid = cursor.fetchone()[0]
        self.conn.commit()
        return hid

    def createGroupChat(self, userid, gname,picture_id):
        cursor = self.conn.cursor()
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        query = "with first_get as(select human_id from users where uid=%s)insert into \
        group_chats(gname,gcreation_date,gpicture_id_path,huid) values(%s,%s,%s,\
        (select human_id from first_get)) returning gid;"
        cursor.execute(query, (userid,gname,date,picture_id,))
        gid = cursor.fetchone()[0]
        self.conn.commit()
        return gid

    def addUserToGroupChat(self, uid, groupchatid):
        cursor = self.conn.cursor()
        query = "insert into ismember(uid,gid) values(%s,%s) returning gid;"
        cursor.execute(query, (uid,groupchatid,))
        gid = cursor.fetchone()[0]
        self.conn.commit()
        return gid

    def deleteGroupChatById(self, gid):
        cursor = self.conn.cursor()
        query = "delete from group_chats where gid = %s;"
        cursor.execute(query, (gid,))
        self.conn.commit()
        return gid

    def deleteGroupChatByName(self, gname):
        cursor = self.conn.cursor()
        query = "delete from group_chats where gid=all(select gid from group_chats where gname=%s);"
        cursor.execute(query, (gname,))
        self.conn.commit()
        return gid

    def deleteMessage(self,mid):
        cursor = self.conn.cursor()
        query = "delete from messages where mid = %s;"
        cursor.execute(query, (mid,))
        self.conn.commit()
        return mid

    def deleteReply(self, rpid):
        cursor = self.conn.cursor()
        query = "delete from replies where rpid = %s;"
        cursor.execute(query, (rpid,))
        self.conn.commit()
        return rpid

    def deleteReaction(self, rid):
        cursor = self.conn.cursor()
        query = "delete from reaction where rid = %s;"
        cursor.execute(query, (rid,))
        self.conn.commit()
        return rid

    def deleteUserFromGroupChat(self, userid,groupchatid):
        cursor = self.conn.cursor()
        query = "delete from ismember where gid = %s and uid=%s;"
        cursor.execute(query, (groupchatid,userid,))
        self.conn.commit()
        return uid

    def updateGroupChat(self, gid, gname,picture):
        cursor = self.conn.cursor()
        query = "update group_chats set gname=%s, gpicture_id_path=%s where gid = %s;"
        cursor.execute(query, (gid, gname,picture,))
        self.conn.commit()
        return gid

    def updateReaction(self, rid, rtype):
        cursor = self.conn.cursor()
        query = "update reactions set rtype=%s where rid=%s;"
        cursor.execute(query, (rtype,rid,))
        self.conn.commit()
        return rid

    def updateMessage(self,mid, mmessage, msize, mlength, mtype, mpath):
        cursor = self.conn.cursor()
        query = "update messages set mmessage=%s, msize = %s, mlength = %s, mtype = %s, mmedia_path = %s where mid = %s;"
        cursor.execute(query, (mmessage, msize, mlength, mtype, mpath,mid,))
        self.conn.commit()
        return mid

    def updateReply(self,rpid,rpreply,rpsize,rplength,rptype,rppath):
        cursor = self.conn.cursor()
        query = "update reply set rpreply= %s, rppicture=%s,rptype=%s, rpsize=%s,rplength=%s where rpid = %s;"
        cursor.execute(query, (rpreply,rppath,rptype,rpsize,rplength,rpid,))
        self.conn.commit()
        return rpid