from config.dbconfig import pg_config
import psycopg2
from flask import jsonify

class UserDAO:

    # def __init__(self):
    connection_url = "user=%s password=%s host=%s port=%s dbname=%s" % (
    pg_config['user'], pg_config['password'], pg_config['host'],
    pg_config["port"], pg_config["dbname"])
    conn = psycopg2.connect(connection_url)

    def registerHuman(self, username, email, password, birth_date, first_name, last_name, phone):
        if username == 'Crystal':
            return 2
        elif username == 'Kahlil':
            return 1
        elif username == 'Alejandro':
            return 3
        else:
            return 69

    def signInUser(self, username, password):
        if username == 'Crystal':
            result = [1, username, '02/25/2019', '02/26/2019']
        elif username == 'Kahlil':
            result = [2, username, '02/25/2019', '02/28/2019']
        elif username == 'Alejandro':
            result = [3, username, '02/25/2019', '02/27/2019']
        else:
            result = [69, username, '03/28/2019', '03/29/2019']
        return result

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select uid, user_name, ucreation_date, umost_recent_login,first_name,last_name from \
            users inner join human on users.human_id=human.huid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByUserId(self, userid):
        cursor = self.conn.cursor()
        query = "select uid, user_name, ucreation_date, umost_recent_login,first_name,last_name from\
             users inner join human on users.human_id=human.huid where users.uid = %s;"
        cursor.execute(query, (userid,))
        result = cursor.fetchone()
        return result

    def getUserInformationByUserId(self, userid):
        cursor = self.conn.cursor()
        query = "select human.huid, first_name,last_name,birthdate,huemail,phone_number,users.uid,user_name,\
        ucreation_date, umost_recent_login from human inner join users on human.huid=users.human_id where users.uid=%s;"
        cursor.execute(query, (userid,))
        result = cursor.fetchone()
        return result

    def getUserInformationByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select human.huid, first_name,last_name,birthdate,huemail,phone_number,users.uid,user_name,\
        ucreation_date, umost_recent_login from human inner join users on human.huid=users.human_id where users.user_name=%s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getUserContactsByUserId(self, userid):
        cursor = self.conn.cursor()
        query = "select users.uid, user_name, ucreation_date, umost_recent_login, first_name,last_name from friends \
                     inner join users on friends.fuid = users.uid inner join human on users.human_id=human.huid where\
                     friends.uid =%s;"
        cursor.execute(query, (userid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select uid, user_name, ucreation_date, umost_recent_login,first_name,last_name from users\
             inner join human on users.human_id=human.huid where users.user_name = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getUserContactsByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select users.uid, user_name, ucreation_date, umost_recent_login, first_name,last_name from friends \
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
        query = "select uid, user_name,ucreation_date,umost_recent_login,first_name,last_name from ismember \
                     natural inner join users inner join human on human.huid=users.human_id where gid = %s AND uid != %s;"
        cursor.execute(query, (groupchatid, userid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    #
    # def update(self, uid):
    #     result = self.getUserById(uid)
    #     result[3] = "UpdateDate 02/26/2019"
    #     return result








