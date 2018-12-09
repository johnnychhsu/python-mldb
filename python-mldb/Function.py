# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-09
# @File Name:          Function.py


class Function(object):

    def __init__(self, connector, dataset):
        self.connector = connector
        self.cursor = connector.cursor()
        self.dataset = dataset

    def show_model(self):
        pass

    def reference(self, model_name, model_type):
        pass

    def classifier(self):
        pass
