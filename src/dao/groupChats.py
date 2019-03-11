import psycopg2
from flask import jsonify

class GroupChatsDAO:


    #def init(self):
       # connection_url = "dbname=%s user=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'])
       #conn = psycopg2.connect(connection_url)

    conn = psycopg2.connect(host = '127.0.0.1', database = 'chatDB', user = 'alejoreyes96', password = 'alejo3579')
