from config.dbconfig import pg_config
import psycopg2
from flask import jsonify
import datetime as dt

class UserDAO:

    # def __init__(self):
    connection_url = "user=%s password=%s host=%s port=%s dbname=%s" % (pg_config['user'], pg_config['password'],\
    pg_config['host'],pg_config["port"], pg_config["dbname"])
    conn = psycopg2.connect(connection_url)

    # insert human
    def registerHumanAndCreateUser(self,first_name,last_name,birth_date,email,password,phone,username):
        cursor = self.conn.cursor()
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        query = "with first_get as(insert into human(first_name,last_name,birthdate,huemail,hupassword,phone_number) \
        values(%s,%s,%s,%s,%s,%s) returning huid) insert into users(human_id,user_name,ucreation_date,\
        umost_recent_login,profile_picture) values((select huid from first_get),%s,%s,%s,null) returning uid;"
        cursor.execute(query, (first_name,last_name,birth_date,email,password,phone,username,date,date,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def registerFriendByUserId(self,userid,friendid):
        cursor = self.conn.cursor()
        query = "insert into friends(fuid,uid) values (%s, %s) returning fuid;"
        cursor.execute(query, (friendid,userid,))
        fuid = cursor.fetchone()[0]
        self.conn.commit()
        return fuid

    def registerFriendByUserEmail(self,userid,friend_email):
        cursor = self.conn.cursor()
        query = "with first_get as(select uid from human inner join users on human.huid=users.human_id where \
        huemail=%s)insert into friends(fuid,uid) values((select uid from first_get),%s) returning fuid;"
        cursor.execute(query, (friend_email,userid,))
        fuid = cursor.fetchone()[0]
        self.conn.commit()
        return fuid

    def signInUser(self, username, password):
        cursor = self.conn.cursor()
        date = dt.datetime.now().strftime("%m/%d/%Y")
        query = "with first_try as(select * from users inner join human on users.human_id=human.huid \
        where user_name=%s and hupassword=%s), second_try as(update users set umost_recent_login=%s where \
        uid=any(select uid from first_try))select uid, user_name, ucreation_date, umost_recent_login,\
        first_name,last_name, profile_picture from first_try;"
        cursor.execute(query,(username,password,date,))
        cursor.execute(query,(username,password,date,))
        result = cursor.fetchone()
        return result

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select uid, user_name, ucreation_date, umost_recent_login,first_name,last_name, profile_picture from \
        users inner join human on users.human_id=human.huid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByUserId(self, userid):
        cursor = self.conn.cursor()
        query = "select uid, user_name, ucreation_date, umost_recent_login,first_name,last_name, profile_picture from\
         users inner join human on users.human_id=human.huid where users.uid = %s;"
        cursor.execute(query, (userid,))
        result = cursor.fetchone()
        return result

    def getUserByUserEmail(self, email):
        cursor = self.conn.cursor()
        query = "select uid from human natural inner join users where huemail = %s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

    def getUserInformationByUserId(self, userid):
        cursor = self.conn.cursor()
        query = "select human.huid, profile_picture, first_name,last_name,birthdate,huemail,phone_number,users.uid,user_name,\
        ucreation_date, umost_recent_login from human inner join users on human.huid=users.human_id where users.uid=%s;"
        cursor.execute(query, (userid,))
        result = cursor.fetchone()
        return result

    def getUserInformationByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select human.huid,  profile_picture, first_name,last_name,birthdate,huemail,phone_number,users.uid,user_name,\
        ucreation_date, umost_recent_login from human inner join users on human.huid=users.human_id where users.user_name=%s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getUserContactsByUserId(self, userid):
        cursor = self.conn.cursor()
        query = "select users.uid,  profile_picture, user_name, ucreation_date, umost_recent_login, first_name,last_name from friends \
                 inner join users on friends.fuid = users.uid inner join human on users.human_id=human.huid where\
                 friends.uid =%s;"
        cursor.execute(query,(userid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select uid, user_name, ucreation_date, umost_recent_login,first_name,last_name, profile_picture from\
         users inner join human on users.human_id=human.huid where users.user_name = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getUserContactsByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select users.uid,  profile_picture, user_name, ucreation_date, umost_recent_login, first_name,last_name from friends \
                inner join users on friends.fuid = users.uid inner join human on users.human_id=human.huid \
                where friends.uid = (select uid from users where user_name = %s);"
        cursor.execute(query, (username,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatsByUserId(self, userid):
        cursor = self.conn.cursor()
        query = 'select * from groupchats natural inner join ismember \
                natural inner join users where uid = %s;'
        cursor.execute(query, (userid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersInGroupChatByUserIdAndGroupChatId(self, userid, groupchatid):
        cursor = self.conn.cursor()
        query = "select uid, user_name,  profile_picture, ucreation_date,umost_recent_login,first_name,last_name from ismember \
                 natural inner join users inner join human on human.huid=users.human_id where gid = %s;"
        cursor.execute(query, (groupchatid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOwnerOfGroupChatById(self, groupchatid):
        cursor = self.conn.cursor()
        query = 'select users.uid,  profile_picture, user_name, ucreation_date, umost_recent_login, first_name,last_name\
        from groupChats inner join Human on groupChats.huid=human.huid inner join users on \
        users.human_id=human.huid where groupChats.gid=%s;'
        cursor.execute(query, (groupchatid,))
        result = cursor.fetchone()
        return result

    def getFriendByUserId(self,fuid):
        cursor = self.conn.cursor()
        query = "select fuid from friends natural inner join users where users.uid=%s;"
        cursor.execute(query, (fuid,))
        result = cursor.fetchone()
        return result

    def getFriendByUserName(self, fname):
        cursor = self.conn.cursor()
        query = "select fuid from friends inner join users on users.uid=friends.uid where \
        fuid=any(select uid from users where user_name=%s);"
        cursor.execute(query, (fname,))
        result = cursor.fetchone()
        return result

    def deleteFriendById(self,fuid):
        cursor = self.conn.cursor()
        query = "delete from friends where fuid=%s"
        cursor.execute(query, (fuid,))
        self.conn.commit()
        return fuid

    def deleteFriendByName(self,fname):
        cursor = self.conn.cursor()
        query = "delete from friends where fuid = all(select uid from users where user_name=%s);"
        cursor.execute(query, (fname,))
        self.conn.commit()
        return fuid

    def deleteFriendByName(self, fname):
        cursor = self.conn.cursor()
        query = "delete from friends where fuid = all(select uid from users where user_name=%s);"
        cursor.execute(query, (fname,))
        self.conn.commit()
        return fname

    def updateUser(self, uid, username, password, birth_date, first_name, last_name, email, phone, profile_picture):
        cursor = self.conn.cursor()
        uid2 = uid
        query = "with first_up as(update users set user_name=%s,profile_picture=%s where uid=%s), \
        second_thing as(select huid from human inner join users on users.human_id=human.huid where users.uid=%s), \
        update human set hupassword=%s,birthdate=%s,first_name=%s,last_name=%s,huemail=%,phone_number=%s \
        where huid=any(select huid from second_thing);"
        cursor.execute(query, (username, profile_picture, uid,uid2,password,birth_date,first_name,last_name,email,phone))
        self.conn.commit()
        return fuid

    def deleteAccount(self,uid):
        cursor = self.conn.cursor()
        query = "delete from human where huid=(select huid from human inner join users on \
        human.huid=users.human_id where users.uid=%s);"
        cursor.execute(query, (uid,))
        self.conn.commit()
        return uid
