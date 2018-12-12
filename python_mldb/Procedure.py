# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-09
# @File Name:          Procedure.py
from sklearn.ensemble import RandomForestClassifier


class Procedure(object):

    def __init__(self, query_handler, dataset):
        self.query_handler = query_handler
        self.dataset = dataset
        self.model_list = []

    def show_progress(self):
        pass

    def save_to_db(self):
        pass


class ClassifierProcedure(Procedure):

    def __init__(self, name, description):
        super(ClassifierProcedure, self).__init__()
        self.name = name
        self.description = description

    def train(self, dataset):
        pass


class RFClassifierProcedure(ClassifierProcedure):

    def __init__(self, name):
        super(RFClassifierProcedure, self).__init__(name)

    def train(self, dataset):
        self._train(dataset)

    def _train(self, dataset):
        pass
