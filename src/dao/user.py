
#from config.dbconfig import pg_config
import psycopg2
from flask import jsonify
import datetime as dt

class UserDAO:

    # def __init__(self):
    #connection_url = "user=%s password=%s host=%s port=%s dbname=%s" % (pg_config['user'], pg_config['password'],\
    # pg_config['host'],pg_config["port"], pg_config["dbname"])
    #conn = psycopg2.connect(connection_url)
    conn = psycopg2.connect(host='127.0.0.1', database='appdb',user='kahlil', password='password')

    # insert human
    def registerHuman(self,first_name,last_name,birth_date,email,password,phone,username,profile_pic):
        cursor = self.conn.cursor()
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        query = "with first_get as(insert into human(first_name,last_name,birthdate,huemail,hupassword,phone_number) \
        values(%s,%s,%s,%s,%s,%s) returning huid) insert into users(human_id,user_name,ucreation_date,umost_\
        recent_login,profile_pic) values((select huid from first_get),%s,%s,%s,%s) returning uid;"
        cursor.execute(query, (first_name,last_name,birth_date,email,password,phone,username,date,date,profile_pic))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def registerFriendByUserId(self,userid,friendid):
        cursor = self.conn.cursor()
        query = "insert into friends(fuid,uid) values (%s, %s) returning fuid;"
        cursor.execute(query, (friendid,userid))
        fuid = cursor.fetchone()[0]
        self.conn.commit()
        return fuid

    def registerFriendByUserEmail(self,userid,friend_email):
        cursor = self.conn.cursor()
        query = "with first_get as(select uid from human inner join users on human.huid=users.human_id where \
        huemail=%s)insert into friends(fuid,uid) values((select uid from first_get),%s) returning fuid;"
        cursor.execute(query, (friend_email,userid))
        fuid = cursor.fetchone()[0]
        self.conn.commit()
        return fuid

    #def signInUser(self, username, password):
     #   if username == 'Crystal':
      #      result = [1, username, '02/25/2019', '02/26/2019']
       # elif username == 'Kahlil':
        #    result = [2, username, '02/25/2019', '02/28/2019']
       # elif username == 'Alejandro':
        #    result = [3, username, '02/25/2019', '02/27/2019']
       # else:
        #    result = [69, username, '03/28/2019', '03/29/2019']
       # return result

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
        ucreation_date, umost_recent_login from human inner join users on human.huid=users.human where users.user_name=%s;"
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
        query = "select uid, user_name,  profile_picture, ucreation_date, umost_recent_login,first_name,last_name from users\
         inner join human on users.human_id=human.huid where users.user_name = %s;"
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
