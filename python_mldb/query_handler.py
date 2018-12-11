# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-09
# @File Name:          query_handler.py


class QueryHandler(object):

    def __init__(self, connector, cursor):
        self.connector = connector
        self.cursor = cursor

    def run_query(self, query):
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as err:
            self._error_handler(err)
        else:
            print ("Query Done.")

    def commit_query(self):
        self.cursor.commit()

    @staticmethod
    def _error_handler(err):
        print("Failed : {}".format(err))

