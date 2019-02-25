from flask import Flask, jsonify, request, redirect, url_for
from handler.groupChats import ChatHandler
from handler.user import UserHandler
from flask_cors import CORS, cross_origin


#Activate
app = Flask(__name__)
#Apply CORS to app
CORS(app)

@app.route('/')
def greeting():
    return 'This is the opening page of the chats app Fast Friends Media!'

@app.route('/register/')
@app.route('/register')
def register():
    return 'Register for the FFM!'
    #

@app.route('/register/<userName>/', methods=['POST'])
@app.route('/register/<userName>', methods=['POST'])
def registerUser(userName):
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UserHandler().createNewUser(userName, request.json)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/sign-in/')
@app.route('/sign-in')
def signInPage():
    return 'This is the sign in page'

@app.route('/sign-in/<id>/')
@app.route('/sign-in/<id>')
def signIn(id):
    return redirect(url_for('getAllGroupChats', userid = id))

@app.route('/<userid>/groupChats/', methods=['GET', 'POST'])
@app.route('/<userid>/groupChats', methods=['GET', 'POST'])
def getAllGroupChats(userid):
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return ChatHandler().createGroupChatJson(request.json)
    else:
        # if not request.args:
            return ChatHandler().getAllGroupChats(userid)
        # else:
        #     return ChatHandler().searchGroupChats(request.args)
#    return 'This is the route to the list of groups of user number: %s' % user_id

@app.route('/<userName>/groupChats/Chat/<int:groupChatId>/', methods=['GET', 'PUT', 'DELETE'])
@app.route('/<userName>/groupChats/Chat/<int:groupChatId>', methods=['GET', 'PUT', 'DELETE'])
def getGroupChatById(userName, groupChatId):

    if request.method == 'GET':
        return ChatHandler().getGroupChatById(groupChatId, userName)
    elif request.method == 'PUT':
        return ChatHandler().updateGroupChat(groupChatId, userName, request.form)
    elif request.method == 'DELETE':
        return ChatHandler().deleteGroupChat(groupChatId, userName)
    else:
        return ChatHandler().getAllGroupChats(userName)

 #   return 'This is group %s : whose name is' % group_name
#

@app.route('/<userid>/groupChats/Chat/<int:groupChatId>/messages/', methods=['GET', 'POST'])
@app.route('/<userid>/groupChats/Chat/<int:groupChatId>/messages', methods=['GET', 'POST'])
def getAllMessages(userid, groupChatId):

    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().createMessageJson(groupChatId, userid, request.json)
    else:
        # if not request.args:
        return ChatHandler().getAllMessages(groupChatId, userid)
        # else:
        #     return ChatHandler().searchGroupChats(request.args)

@app.route('/<userid>/groupChats/Chat/<int:groupChatId>/messages/<int:messageid>/', methods=['GET', 'PUT', 'DELETE'])
@app.route('/<userid>/groupChats/Chat/<int:groupChatId>/messages/<int:messageid>', methods=['GET', 'PUT', 'DELETE'])
def getMessagesById(userid, groupChatId, messageid):
    if request.method == 'GET':
        return ChatHandler().getMessageById(groupChatId, userid, messageid)
    elif request.method == 'PUT':
        return ChatHandler().updateMessage(groupChatId, userid, messageid, request.form)
    elif request.method == 'DELETE':
        return ChatHandler().deleteMessage(groupChatId, userid, messageid)
    else:
        return ChatHandler().getAllGroupChats(userid)

@app.route('/<userid>/groupChats/Chat/<int:groupChatId>/messages/<int:messageid>/like/', methods=['PUT'])
@app.route('/<userid>/groupChats/Chat/<int:groupChatId>/messages/<int:messageid>/like', methods=['PUT'])
def likeMedia(userid, groupChatId, messageid):
    return ChatHandler().likeMessage(groupChatId, userid, messageid)

@app.route('/<userid>/groupChats/Chat/<int:groupChatId>/messages/<int:messageid>/dislike/', methods=['PUT'])
@app.route('/<userid>/groupChats/Chat/<int:groupChatId>/messages/<int:messageid>/dislike', methods=['PUT'])
def dislikeMedia(userid, groupChatId, messageid):
    return ChatHandler().dislikeMessage(groupChatId, userid, messageid)

@app.route('/<userid>/Profile/', methods=['GET', 'PUT'])
@app.route('/<userid>/Profile', methods=['GET', 'PUT'])
def getProfile(userid):
    if request.method == 'GET':
        if not userid == 'all':
            return UserHandler().getUserbyId(userid)
        else:
            return UserHandler().getAllUsers()
    elif request.method == 'PUT':
        return UserHandler().updateUser(userid, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405



if __name__ == '__main__':
    app.run(debug=True)