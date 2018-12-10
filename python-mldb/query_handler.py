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
        pass

    def _error_handler(self):
        pass

