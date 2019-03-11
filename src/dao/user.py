import psycopg2
from flask import jsonify


class UserDAO:

    # def _init_(self):
    # connection_url = "dbname=appdb user=roxy password=passsword"# pg_config['dbname'], pg_config['user'], pg_config['password'])

    conn = psycopg2.connect(host='127.0.0.1', database='chatDB', user='alejoreyes96', password='alejo3579')

