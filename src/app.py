from flask import Flask, jsonify, request, redirect, url_for
from handler.groupChats import ChatHandler
from handler.user import UserHandler

#Activate
app = Flask(__name__)


@app.route('/')
def greeting():
    return 'This is the opening page of the chats app Fast Friends Media!'

#@app.route('/', methods=['POST'])
@app.route('/register')
def register():
    return 'Register for the FFM!'
    # if request.method == 'POST':
    #     print("REQUEST: ", request.json)
    #     return UserHandler().createNewUser(request.json)
    # else:
    #     return jsonify(Error="Method not allowed."), 405


#    return 'This is the route to the registry page'

@app.route('/sign-in')
def signInPage():
    return 'This is the sign in page'


@app.route('/sign-in/<id>')
def signIn(id):
    return redirect(url_for('getAllGroupChats', userid = id))

@app.route('/<userid>/groupChats', methods=['GET', 'POST'])
def getAllGroupChats(userid):
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return ChatHandler().insertGroupChatJson(request.json)
    else:
        if not request.args:
            return ChatHandler().getAllGroupChats(userid)
        else:
            return ChatHandler().searchGroupChats(request.args)
#    return 'This is the route to the list of groups of user number: %s' % user_id

@app.route('/<userid>/groupChats/Chat/<int:groupChatId>', methods=['GET', 'PUT', 'DELETE'])
def getGroupChatById(userid, groupChatId):

    if request.method == 'GET':
        return ChatHandler().getGroupChatById(groupChatId, userid)
    elif request.method == 'PUT':
        return ChatHandler().updateGroupChat(groupChatId, request.form)
    elif request.method == 'DELETE':
        return ChatHandler().deleteGroupChat(groupChatId)
    else:
        return ChatHandler().getAllGroupChats(userid)

 #   return 'This is group %s : whose name is' % group_name
#
@app.route('/<userid>/groupChats/Chat/<int:groupChatId>/messages', methods=['GET', 'PUT', 'DELETE'])
def getAllMessages(userid, groupChatId):
    if request.method == 'GET':
        return ChatHandler().getAllMessages(groupChatId, userid)
    elif request.method == 'PUT':
        return ChatHandler().updateGroupChat(groupChatId, request.form)
    elif request.method == 'DELETE':
        return ChatHandler().deleteGroupChat(groupChatId)
    else:
        return ChatHandler().getAllGroupChats(userid)

@app.route('/<userid>/Profile', methods=['GET'])
def getProfile(userid):
    if request.method == 'GET':
        if not userid == 'all':
            return UserHandler().getUserbyId(userid)
        else:
            return UserHandler().getAllUsers()
    else:

        return jsonify(Error="Method not allowed."), 405


    #return 'Welcome to %s profile page, where you can see which group she is a part of.' % user




if __name__ == '__main__':
    app.run(debug=True)