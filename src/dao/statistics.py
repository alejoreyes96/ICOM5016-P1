import psycopg2
import datetime as dt

class StatsDAO:
    # def __init__(self):
    # connection_url = "user=%s password=%s host=%s port=%s dbname=%s" % (pg_config['user'], pg_config['password'],\
    # pg_config['host'],pg_config["port"], pg_config["dbname"])
    # conn = psycopg2.connect(connection_url)
    conn = psycopg2.connect(host='127.0.0.1', database='chatDB',user='alejoreyes96', password='alejo3579')


    def getAllUserCount(self):
        cursor = self.conn.cursor()
        query = "select count(*) from users;"
        cursor.execute(query, )
        result = cursor.fetchone()
        return result

    def getMostPopularHashtags(self):
        cursor = self.conn.cursor()
        query = "select max(number_of_times),hhashtag from (select hhashtag,count(contains.hid) as number_of_times\
    	from hashtags natural inner join contains group by hhashtag)hashtags group by hhashtag order by max desc \
    	limit 3;"
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesCount(self):
        cursor = self.conn.cursor()
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        query = "select count(*) from messages where mupload_date=%s;"
        cursor.execute(query,(date,))
        result = cursor.fetchone()
        return result

    def getAllRepliesCount(self):
        cursor = self.conn.cursor()
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        query = "select count(*) from replies where rpupload_date=%s;"
        cursor.execute(query,(date,))
        result = cursor.fetchone()
        return result

    def getAllGroupChatsCount(self):
        cursor = self.conn.cursor()
        query = "select count(*) from groupChats;"
        cursor.execute(query, )
        result = cursor.fetchone()
        return result

    def getAllLikesCount(self):
        cursor = self.conn.cursor()
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        query = 'select count(*) from reactions where rupload_date=%s and rtype=true;'
        cursor.execute(query,(date,) )
        result = cursor.fetchone()
        return result

    def getAllDislikesCount(self):
        cursor = self.conn.cursor()
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        query = 'select count(*) from reactions where rupload_date=%s and rtype=false;'
        cursor.execute(query, (date,))
        result = cursor.fetchone()
        return result

    def getAllPostsByUserId(self,uid):
        cursor = self.conn.cursor()
        query = 'select count(*) from messages where mupload_date=%s and uid=%s;'
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        cursor.execute(query,(date,uid,))
        result = cursor.fetchone()
        return result

    def getRepliesforPictures(self,mmedia_path):
        cursor = self.conn.cursor()
        query = 'select count(replies.mid) from messages inner join replies on replies.mid=messages.mid \
        where mmedia_path=%s;'
        cursor.execute(query, (mmedia_path,))
        result = cursor.fetchone()
        return result

    def getLikesforPictures(self,mmedia_path):
        cursor = self.conn.cursor()
        query = 'select count(reactions.mid)from messages inner join reactions on reactions.mid=messages.mid\
        where mmedia_path=%s and reactions.rtype=true;'
        cursor.execute(query, (mmedia_path,))
        result = cursor.fetchone()
        return result

    def getDislikesforPictures(self,mmedia_path):
        cursor = self.conn.cursor()
        query = 'select count(reactions.mid)from messages inner join reactions on reactions.mid=messages.mid\
        where mmedia_path=%s and reactions.rtype=false;'
        cursor.execute(query,(mmedia_path,) )
        result = cursor.fetchone()
        return result

    def getMostActiveUsers(self):
        cursor = self.conn.cursor()
        query='select user_name, uid from users where umost_recent_login=%s limit 3;'
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        cursor.execute(query,(date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesPerDay(self):
        cursor = self.conn.cursor()
        date = dt.datetime.now().strftime("%m/%d/%Y")
        query = "select mupload_date, count(mupload_date) from messages where mupload_date between '01/01/2017' and %s group by mupload_Date order by mupload_date;"
        cursor.execute(query,(date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRepliesPerDay(self):
        cursor = self.conn.cursor()

        date = dt.datetime.now().strftime("%m/%d/%Y")
        query = "select rpupload_date, count(rpupload_date) from replies where rpupload_date between '01/01/2017' and %s group by rpupload_date order by rpupload_date;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getLikesPerDay(self):
        cursor = self.conn.cursor()

        date = dt.datetime.now().strftime("%m/%d/%Y")
        query = "select rupload_date, count(rupload_date) from reactions where rupload_date between '01/01/2017' and %s and rtype=true group by rupload_Date order by rupload_date;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDislikesPerDay(self):
        cursor = self.conn.cursor()

        date = dt.datetime.now().strftime("%m/%d/%Y")
        query = "select rupload_date, count(rupload_date) from reactions where rupload_date between '01/01/2017' and %s and rtype=false group by rupload_Date order by rupload_date;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result