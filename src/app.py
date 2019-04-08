from flask import Flask, jsonify, request, redirect, url_for
from handler.groupChats import ChatHandler
from handler.user import UserHandler
from flask_cors import CORS
from handler.statistics import StatsHandler

#Activate
app = Flask(__name__)
CORS(app)

# Default route
@app.route('/')
def greeting():
    return 'This is the opening page of the Fast Friends Media App!'

# SIGN IN and SIGN UP routes
# Register human route
@app.route('/FFMA/register/', methods=['GET', 'POST'])
@app.route('/FFMA/register', methods=['GET', 'POST'])
def registerHuman():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UserHandler().registerHuman(request.json)
    else:
        return jsonify(Error="Method not allowed."), 405

# User sign-in route
@app.route('/FFMA/sign-in/', methods=['GET', 'POST'])
@app.route('/FFMA/sign-in', methods=['GET', 'POST'])
def signInUser():
    if request.method == 'POST':
        return UserHandler().signInUser(request.json)
    else:
        return jsonify(Error="Method not allowed."), 405

#Users
# View all users of the FFMA
@app.route('/FFMA/users/')
@app.route('/FFMA/users')
def getAllUsers():
    return UserHandler().getAllUsers()

# View user by id
@app.route('/FFMA/users/<int:userid>/')
@app.route('/FFMA/users/<int:userid>')
def getUserByUserId(userid):
    return UserHandler().getUserByUserId(userid)

# View user information by id
@app.route('/FFMA/users/<int:userid>/profile/')
@app.route('/FFMA/users/<int:userid>/profile')
def getUserInformationByUserId(userid):
    return UserHandler().getUserInformationByUserId(userid)

# View user contact information by id
@app.route('/FFMA/users/<int:userid>/contacts/')
@app.route('/FFMA/users/<int:userid>/contacts')
def getUserContactsByUserId(userid):
    return UserHandler().getUserContactsByUserId(userid)

# View user by username
@app.route('/FFMA/users/<string:username>/')
@app.route('/FFMA/users/<string:username>')
def getUserByUsername(username):
    return UserHandler().getUserByUsername(username)

# View user contact information by username
@app.route('/FFMA/users/<string:username>/contacts/')
@app.route('/FFMA/users/<string:username>/contacts')
def getUserContactsByUsername(username):
    return UserHandler().getUserContactsByUsername(username)


# View user group chats or create one
@app.route('/FFMA/users/<int:userid>/groupChats/', methods=['GET', 'POST'])
@app.route('/FFMA/users/<int:userid>/groupChats', methods=['GET', 'POST'])
def getAvailableGroupChatsByUserId(userid):
    if request.method == 'GET':
        return ChatHandler().getAvailableGroupChatsByUserId(userid)
    else:
        return ChatHandler().createGroupChat(userid, request.json)


@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/', methods=['GET', 'PUT', 'DELETE'])
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>', methods=['GET', 'PUT', 'DELETE'])
def getGroupChatById(userid, groupchatid):
    if request.method == 'PUT':
        return ChatHandler().updateGroupChat(groupchatid, request.json)
    elif request.method == 'DELETE':
        return ChatHandler().deleteGroupChat(groupchatid)
    else:
        return ChatHandler().getGroupChatById(groupchatid)

# View messages by hash-tag string
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/hashtags/<string:hashtagstring>/')
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/hashtags/<string:hashtagstring>')
def getMessagesByHashtagStringInGroupChat(userid, groupchatid, hashtagstring):
        return ChatHandler().getMessagesByHashtagStringInGroupChat(userid, groupchatid, hashtagstring)

# View messages on a group chat or post one
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/', methods=['GET', 'POST'])
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages', methods=['GET', 'POST'])
def getMessagesFromGroupChatByUserIdAndGroupChatId(userid, groupchatid):
    if request.method == 'GET':
        return ChatHandler().getMessagesFromGroupChatByUserIdAndGroupChatId(userid, groupchatid)
    else:
        return ChatHandler().postMessage(userid, groupchatid, request.json)

# view messages by id
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/', methods=['GET', 'PUT', 'DELETE'])
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>', methods=['GET', 'PUT', 'DELETE'])
def getMessagesFromGroupChatById(userid, groupchatid, messageid):
    if request.method == 'PUT':
        return ChatHandler().updateMessage(userid, groupchatid, messageid, request.json)
    elif request.method == 'GET':
        return ChatHandler().getMessageFromGroupChatById(userid, groupchatid, messageid)
    else:
        return ChatHandler().deleteMessage(groupchatid, messageid)

# View likes of a message in a group chat or like it
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/reactions/', methods=['GET', 'POST'])
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/reactions', methods=['GET', 'POST'])
def getMessageReactionsInGroupChatByUserIdAndGroupChatIdAndMessageId(userid, groupchatid, messageid):
    if request.method == 'GET':
        return ChatHandler().getMessageReactionsInGroupChatByUserIdAndGroupChatIdAndMessageId(userid, groupchatid, messageid)

    else:
        return ChatHandler().addReaction(userid, groupchatid, messageid, request.json)

@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/reactions/<int:rid>/',
           methods=['GET', 'PUT', 'DELETE'])
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/reactions/<int:rid>',
           methods=['GET', 'PUT', 'DELETE'])
def getMessageReactionsById(userid, groupchatid, messageid, rid):
    if request.method == 'PUT':
        return ChatHandler().updateReaction(groupchatid, messageid, rid, request.json)

    elif request.method == 'DELETE':
        return ChatHandler().deleteReaction(groupchatid, messageid, rid)
    else:
        return ChatHandler().getMessageReactionsById(userid, groupchatid, messageid, rid)

@app.route('/FFMA/messages/')
def getAllMessages():
    return ChatHandler().getAllMessages()

@app.route('/FFMA/groupChats/')
def getAllGroupChats():
    return ChatHandler().getAllGroupChats()

@app.route('/FFMA/messages/<int:messageid>/reactions/likes/')
def getMessageLikesByMessageId(messageid):
    return ChatHandler().getMessageLikesByMessageId(messageid)

@app.route('/FFMA/messages/<int:messageid>/reactions/dislikes/')
def getMessageDislikesByMessageId(messageid):
    return ChatHandler().getMessageDislikesByMessageId(messageid)

# View replies of a message in a group chat or reply to it
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/replies/', methods=['GET', 'POST'])
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/replies', methods=['GET', 'POST'])
def getRepliesFromMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(userid, groupchatid, messageid):
    if request.method == 'POST':
        return ChatHandler().replyToMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(userid, groupchatid, messageid, request.json)

    else:
        return ChatHandler().getRepliesFromMessageInGroupChatByUserIdAndGroupChatIdAndMessageId(userid, groupchatid, messageid)

@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/replies/<int:replyid>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/replies/<int:replyid>', methods=['GET', 'PUT', 'DELETE'])
def getRepliesById(userid, groupchatid, messageid, replyid):
    if request.method == 'PUT':
        return ChatHandler().updateReply(userid, groupchatid, messageid, replyid, request.json)
    elif request.method == 'DELETE':
        return ChatHandler().deleteReply(userid, groupchatid, messageid, replyid)
    else:
        return ChatHandler().getReplyById(userid, groupchatid, messageid, replyid)

# View all users in a group chat
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/users/', methods=['GET', 'POST'])
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/users', methods=['GET', 'POST'])
def getUsersInGroupChatByUserIdAndGroupChatId(userid, groupchatid):
    if request.method == 'GET':
        return UserHandler().getUsersInGroupChatByUserIdAndGroupChatId(userid, groupchatid)
    else:
        return ChatHandler().addUserToGroupChat(userid, groupchatid, request.json)

@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/users/<userid2>/', methods=['GET', 'DELETE'])
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/users/<userid2>', methods=['GET', 'DELETE'])
def deleteUserFromGroupChatById(userid, userid2, groupchatid):
    if request.method == 'DELETE':
        return ChatHandler().deleteUserFromGroupChatById(userid, userid2, groupchatid)
    else:
        return jsonify(Error="Method not allowed."), 405


# View likes of a message in a group chat or like it
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/reactions/likes/')
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/reactions/likes')
def getMessageLikesInGroupChatByUserIdAndGroupChatIdAndMessageId(userid,groupchatid, messageid):
    if request.method == 'GET':
        return ChatHandler().getMessageLikesInGroupChatByUserIdGroupChatIdAndMessageId(groupchatid, messageid)

# View dislikes of a message in a group chat or like it
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/reactions/dislikes/')
@app.route('/FFMA/users/<int:userid>/groupChats/<int:groupchatid>/messages/<int:messageid>/reactions/dislikes')
def getMessageDislikesInGroupChatByUserIdAndGroupChatIdAndMessageId(userid,groupchatid, messageid):
    if request.method == 'GET':
        return ChatHandler().getMessageDislikesInGroupChatByUserIdGroupChatIdAndMessageId(userid,groupchatid, messageid)

@app.route('/FFMA/groupChats/<int:groupchatid>/owner/')
def getOwnerOfGroupChatById(groupchatid):
    return UserHandler().getOwnerOfGroupChatById(groupchatid)

@app.route('/FFMA/groupChats/<int:groupchatid>/')
def getGroupChatInfoById(groupchatid):
    return ChatHandler().getGroupChatInfoById(groupchatid)

# View user information by username
@app.route('/FFMA/users/<string:username>/profile/')
@app.route('/FFMA/users/<string:username>/profile')
def getUserInformationByUsername(username):
    return UserHandler().getUserInformationByUsername(username)

@app.route('/FFMA/Stats')
def getStats():
    return StatsHandler().getAllStats()


@app.route('/FFMA/Stats/Picture/<string:picture_name>')
def getStatsForPictures(picture_name):
    return StatsHandler().getStatsForPictures(picture_name)

@app.route('/FFMA/Stats/Hashtags')
def getStatsForHashtags():
    return StatsHandler().getMostPopularHashtags()

@app.route('/FFMA/Stats/Users')
def getStatsForUserActivity():
    return StatsHandler().getMostActiveUsers()

if __name__ == '__main__':
    app.run(debug=True)