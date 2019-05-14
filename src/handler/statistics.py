from flask import jsonify
from dao.statistics import StatsDAO

class StatsHandler:


    def build_stats_dict(self,row):
        result = {}
        result['Number of Users In System'] = row[0]
        result['Number of GroupChats In System'] = row[1]
        return result

    def build_stats_attr(self,uids,gids):
        result = {}
        result['Number of Users In System'] = uids
        result['Number of GroupChats In System'] = gids
        return result

    def build_stats_specific_user_dict(self,row):
        result={}
        result['Messages by User'] = row[0]
        return result

    def build_stats_specific_attr(self,mids):
        result={}
        result['Messages by User'] = mids
        return result

    def build_stats_specific_pict_dict(self,row):
        result={}
        result['Replies to a Photo'] = row[0]
        result['LIkes to a Photo'] = row[1]
        result['Dislikes to a Photo'] = row[2]
        return result

    def build_stats_specific_pict_attr(self,rp,likes,dislikes):
        result={}
        result['Replies to a Photo'] = rp
        result['LIkes to a Photo'] = likes
        result['Dislikes to a Photo'] = dislikes
        return result

    def build_stats_popularity_dict(self,row):
        result={}
        result['Top Hashtags'] = row[0]
        result['Hashtag']=row[1]
        return result

    def build_stats_user_popularity_dict(self,row):
        result={}
        result['Top Most Active User']=row[0]
        result['UID']=row[1]
        return result

    def build_stats_popularity_attr(self,hid1):
        result={}
        result['Hashtags #1']=hid1
        return result

    def build_stats_users_popularity_attr(self,mau1,mau2):
        result={}
        result['Most Active User #1']=mau1
        result['UID']=mau2
        return result

    def getAllStats(self):
        dao = StatsDAO()
        stats = []
        stats.append(dao.getAllUserCount())
        stats.append(dao.getAllGroupChatsCount())
        result_map = self.build_stats_attr(stats[0], stats[1])
        return jsonify(Stats=result_map),201


    def getStatsForPictures(self,picture_name):
        dao = StatsDAO()
        stats = []
        stats.append(dao.getRepliesforPictures(picture_name))
        stats.append(dao.getLikesforPictures(picture_name))
        stats.append(dao.getDislikesforPictures(picture_name))
        result_map = self.build_stats_specific_pict_attr(stats[0],stats[1],stats[2])
        return jsonify(Stats=result_map),201

    def getMostActiveUsers(self):
        dao = StatsDAO()
        user_list = dao.getMostActiveUsers()
        result_map = []
        for row in user_list:
            result = self.build_stats_user_popularity_dict(row)
            result_map.append(result)
        return jsonify(Stats=result_map)

    def getMostPopularHashtags(self):
        dao = StatsDAO()
        user_list = dao.getMostPopularHashtags()
        result_map = []
        for row in user_list:
            result = self.build_stats_popularity_dict(row)
            result_map.append(result)
        return jsonify(Stats=result_map)

    def build_stats_user_post_dict(self,row):
        result={}
        result['Amount Per Day'] = str(row[0])
        result['Date'] = row[1]
        return result

    def getAllPostsByUserIdPerDay(self,userid):
        dao = StatsDAO()
        day_list = dao.getAllPostsByUserIdPerDay(userid)
        result_map = []
        if day_list is None:
            return jsonify(Error="User doesn't exist!")
        else:
            if len(day_list)==0:
                return jsonify(Error="User doesn't exist!")
            elif len(day_list) <2:
                result_map.append(self.build_stats_user_post_dict(day_list))
            else:
                for row in day_list:
                    result = self.build_stats_user_post_dict(row)
                    result_map.append(result)
        return jsonify(Stats=result_map)

    def build_stats_message_perday_dict(self,row):
        result={}
        result['Amount Per Day'] = str(row[0])
        result['Date'] = row[1]
        return result

    def getAllMessagesPerDay(self):
        dao = StatsDAO()
        day_list = dao.getAllMessagesPerDay()
        result_map = []
        if day_list is None:
            return jsonify(Error="NO Messages exist!")
        else:
            if len(day_list)==0:
                return jsonify(Error="No Messages exist!")
            elif len(day_list) <2:
                result_map.append(self.build_stats_message_perday_dict(day_list))
            else:
                for row in day_list:
                    result = self.build_stats_message_perday_dict(row)
                    result_map.append(result)
        return jsonify(Stats=result_map)



    def build_stats_replies_perday_dict(self,row):
        result={}
        result['Amount Per Day'] = str(row[0])
        result['Date'] = row[1]
        return result

    def getAllRepliesPerDay(self):
        dao = StatsDAO()
        day_list = dao.getAllRepliesPerDay()
        result_map = []
        if day_list is None:
            return jsonify(Error="No Replies exist!")
        else:
            if len(day_list)==0:
                return jsonify(Error="No Replies exist!")
            elif len(day_list) <2:
                result_map.append(self.build_stats_replies_perday_dict(day_list))
            else:
                for row in day_list:
                    result = self.build_stats_replies_perday_dict(row)
                    result_map.append(result)
        return jsonify(Stats=result_map)


    def build_stats_likes_perday_dict(self,row):
        result={}
        result['Amount Per Day'] = str(row[0])
        result['Date'] = row[1]
        return result

    def getAllLikesPerDay(self):
        dao = StatsDAO()
        day_list = dao.getAllLikesPerDay()
        result_map = []
        if day_list is None:
            return jsonify(Error="No LIkes exist!")
        else:
            if len(day_list)==0:
                return jsonify(Error="No LIkes exist!")
            elif len(day_list) <2:
                result_map.append(self.build_stats_likes_perday_dict(day_list))
            else:
                for row in day_list:
                    result = self.build_stats_likes_perday_dict(row)
                    result_map.append(result)
        return jsonify(Stats=result_map)


    def build_stats_dislike_perday_dict(self,row):
        result={}
        result['Amount Per Day'] = str(row[0])
        result['Date'] = row[1]
        return result

    def getAllDislikesPerDay(self):
        dao = StatsDAO()
        day_list = dao.getAllDislikesPerDay()
        result_map = []
        if day_list is None:
            return jsonify(Error="No Dislikes exist!")
        else:
            if len(day_list)==0:
                return jsonify(Error="No Dislikes exist!")
            elif len(day_list) <2:
                result = self.build_stats_dislike_perday_dict(day_list)
                result_map.append(result)
            else:
                for row in day_list:
                    result = self.build_stats_dislike_perday_dict(row)
                    result_map.append(result)
        return jsonify(Stats=result_map)