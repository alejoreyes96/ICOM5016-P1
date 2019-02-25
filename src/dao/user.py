from flask import jsonify

class UserDAO:

    def insert(self, huname, huemail, hupassword, hubirthDate, huphoneNum):
        huid = 4
        return huid

    def getAllUsers(self):
        result = [[1, 'Crystal', '6', '12/12/2018'], [2, 'Kahlil', '752', '02/23/2019'], [3, 'Alejandro', '1695', '02/24/2019']]
        return result

    def getUserById(self, uid):
        if uid == 'Alejandro':
            result = [3, 'Alejandro', '1695', '02/24/2019']
        elif uid == 'Kahlil':
            result = [2, 'Kahlil', '752', '02/23/2019']
        elif uid == 'Crystal':
            result = [1, 'Crystal', '6', '12/12/2018']
        else:
            result = []
        return result


    def delete(self, huid):
        huid = 1
        return huid


    def update(self, uid):
        result = self.getUserById(uid)
        result[3] = "UpdateDate 02/26/2019"
        return result








