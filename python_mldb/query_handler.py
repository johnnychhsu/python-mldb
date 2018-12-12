# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-11
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
            print ("Query: {} done.".format(query))
            return self._db_result()

    @staticmethod
    def _error_handler(err):
        print("Failed : {}".format(err))

    def _db_result(self):
        # item is tuple
        for item in self.cursor:
            yield item
