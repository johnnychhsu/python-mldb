# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-09
# @File Name:          Procedure.py


class Procedure(object):

    def __init__(self, query_handler, dataset):
        self.query_handler = query_handler
        self.dataset = dataset
        self.model_list = []

    def show_progress(self):
        pass

    def train(self, model_name, model_type, dataset):
        pass


class ClassifierProcedure(Procedure):

    def __init__(self):
        super(ClassifierProcedure, self).__init__(Procedure)


