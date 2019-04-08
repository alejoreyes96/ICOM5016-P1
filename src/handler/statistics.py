from flask import jsonify
from dao.statistics import StatsDAO

class StatsHandler:


    def build_stats_dict(self,row):
        result = {}
        result['Number of Users In System'] = row[0]
        result['Number of GroupChats In System'] = row[1]
        result['Number of Posts Per Day'] = row[2]
        result['Number of Replies Per Day'] = row[3]
        result['Number of Likes Per Day'] = row[4]
        result['Number of Dislikes Per Day'] = row[5]
        return result

    def build_stats_attr(self,uids,gids,mids,rpids,likes,dlikes):
        result = {}
        result['Number of Users In System'] = uids
        result['Number of GroupChats In System'] = gids
        result['Number of Posts Per Day'] = mids
        result['Number of Replies Per Day'] = rpids
        result['Number of Likes Per Day'] = likes
        result['Number of Dislikes Per Day'] = dlikes
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
        stats.append(dao.getAllMessagesCount())
        stats.append(dao.getAllRepliesCount())
        stats.append(dao.getAllLikesCount())
        stats.append(dao.getAllDislikesCount())
        result_map = self.build_stats_attr(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5])
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
