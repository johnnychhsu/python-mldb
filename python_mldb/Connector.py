# @Author: Johnny Hsu
# @Date: 2018-12-11
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-11
# @File Name:          Connector.py

import mysql.connector
from mysql.connector import errorcode
from mysql.connector.constants import ClientFlag


class Connector(object):

    def __init__(self, password, host='localhost', user='root'):
        self.host = host
        self.user = user
        self.password = password
        self.mydb = None
        self.cursor = None
        self.db_list = []

    def __del__(self):
        if self.mydb:
            self.mydb.close()
        if self.cursor:
            self.cursor.close()

        print ("Connection finished.")

    def connect(self):
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                auth_plugin='mysql_native_password',
                client_flags=[ClientFlag.LOCAL_FILES]
            )
            self.mydb.autocommit = True

            self.cursor = self.mydb.cursor()

            print ("Connection established.")

            return True

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)




