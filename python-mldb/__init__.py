# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-09
# @File Name:          __init__.py

import mysql.connector
from mysql.connector import errorcode


class Connector(object):

    def __init__(self, password, host='localhost', user='root'):
        self.host = host
        self.user = user
        self.password = password
        self.mydb = None
        self.cursor = None
        self.db_list = []

    def __del__(self):
        self.cursor.close()
        self.mydb.close()

    def connect(self):
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password
            )

            self.cursor = self.mydb.cursor()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def show_database(self):
        pass

    def choose_database(self, db_name):

        self.mydb.database = db_name



