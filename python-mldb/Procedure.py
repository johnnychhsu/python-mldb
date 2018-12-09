# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-09
# @File Name:          Procedure.py


class Procedure(object):

    def __init__(self, connector, dataset):
        self.connector = connector
        self.cursor = connector.cursor()
        self.dataset = dataset

    def show_model(self):
        pass

    def train(self, model_name):
        pass

    def import_raw(self):
        pass
