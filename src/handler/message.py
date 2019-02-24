from flask import jsonify
from dao.message import MessageDAO

class MessageHandler:

    def build_message_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['muserid'] = row[1]
        result['muploadDate'] = row[2]
        result['msize'] = row[3]
        result['mcontent'] = row[4]
        result['mgroupid'] = row[5]
        return result

    def build_reaction_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['ruserid'] = row[1]
        result['ruploadDate'] = row[2]
        result['rlikes'] = row[3]
        result['rdislikes'] = row[4]
        result['rgroupid'] = row[5]
        return result

    def build_picture_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['psize'] = row[1]

        return result
    def build_video_dict(self, row):
        result = {}
        result['vid'] = row[0]
        result['vlength'] = row[1]
        result['vgif'] = row[2]
        return result