import psycopg2
import datetime as dt

class StatsDAO:
    # def __init__(self):
    # connection_url = "user=%s password=%s host=%s port=%s dbname=%s" % (pg_config['user'], pg_config['password'],\
    # pg_config['host'],pg_config["port"], pg_config["dbname"])
    # conn = psycopg2.connect(connection_url)
    conn = psycopg2.connect(host='127.0.0.1',port='5432',user='alejoreyes96',password='alejo3579',dbname='chatDB')


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
    	limit 20;"
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesPerDay(self):
        cursor = self.conn.cursor()
        query = "with first_set as(select * from messages) select count(*),first_set.mupload_date \
        from first_set group by first_set.mupload_date order by first_set.mupload_date desc;"
        cursor.execute(query,())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRepliesPerDay(self):
        cursor = self.conn.cursor()
        date = dt.datetime.now().date().strftime("%m/%d/%Y")
        query = "with first_set as(select * from replies) select count(*),first_set.rpupload_date \
        from first_set group by first_set.rpupload_date order by first_set.rpupload_date desc;"
        cursor.execute(query,())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllGroupChatsCount(self):
        cursor = self.conn.cursor()
        query = "select count(*) from groupChats;"
        cursor.execute(query, )
        result = cursor.fetchone()
        return result

    def getAllLikesPerDay(self):
        cursor = self.conn.cursor()
        query = "with first_set as(select * from reactions where rtype=true) select count(*),first_set.rupload_date \
        from first_set group by first_set.rupload_date order by first_set.rupload_date desc;"
        cursor.execute(query,())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllDislikesPerDay(self):
        cursor = self.conn.cursor()
        query = "with first_set as(select * from reactions where rtype=false) select count(*),first_set.rupload_date \
        from first_set group by first_set.rupload_date order by first_set.rupload_date desc;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllPostsByUserIdPerDay(self,uid):
        cursor = self.conn.cursor()
        query = "with first_set as(select * from messages where uid=%s) select count(*),first_set.mupload_date \
        from first_set group by first_set.mupload_date order by first_set.mupload_date desc;"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
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
