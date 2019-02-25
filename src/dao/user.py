from flask import jsonify

class UserDAO:

    def insert(self, huname, huemail, hupassword, hubirthDate, huphoneNum):
        huid = 0
        return huid


    def getAllUsers(self):
        result = [[1, 'Crystal', '6', '12/12/2018'], [2, 'Kahlil', '752', '02/23/2019'], [3, 'Alejandro', '1695', '02/24/2019']]
        return result

    def getUserById(self, uname):
        if uname == 'Alejandro':
            result = [3, 'Alejandro', '1695', '02/24/2019']
        elif uname == 'Kahlil':
            result = [2, 'Kahlil', '752', '02/23/2019']
        elif uname == 'Crystal':
            result = [1, 'Crystal', '6', '12/12/2018']
        else:
            result = []
        return result

