from flask import Flask, jsonify, request
from handler.groupChats import ChatHandler
from handler.user import UserHandler


#Activate
app = Flask(__name__)


# @app.route('/')
# def greeting():
#     return 'This is the opening page of the chats app jkwrhgaiun'

@app.route('/', methods=['POST'])
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UserHandler().createNewUser(request.json)
    else:
        return jsonify(Error="Method not allowed."), 405


#    return 'This is the route to the registry page'


@app.route('/groupChats/<userid>', methods=['GET', 'POST'])
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

@app.route('/Chat/<int:groupChatId>', methods=['GET', 'PUT', 'DELETE'])
def getGroupChatById(groupChatId):
    if request.method == 'GET':
        return ChatHandler().getGroupChatById(groupChatId)
    elif request.method == 'PUT':
        return ChatHandler().updateGroupChat(groupChatId, request.form)
    elif request.method == 'DELETE':
        return ChatHandler().deleteGroupChat(groupChatId)
    else:
        return jsonify(Error="Method not allowed."), 405

 #   return 'This is group %s : whose name is' % group_name

@app.route('/Profile/<user>')
def profile(user):
    return 'Welcome to %s profile page, where you can see which group she is a part of.' % user





if __name__ == '__main__':
    app.run(debug=True)