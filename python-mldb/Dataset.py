# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-09
# @File Name:          Dataset.py


class Dataset(object):

    def __init__(self, connector):
        self.connector = connector
        self.cursor = connector.cursor()

    def save_to_database(self, name):
        pass

    def load_from_database(self, name):
        pass

