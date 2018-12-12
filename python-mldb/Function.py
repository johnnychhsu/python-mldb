# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-09
# @File Name:          Function.py


class Function(object):

    def __init__(self, query_handler, dataset):
        self.query_handler = query_handler
        self.dataset = dataset

    def show_model(self):
        pass

    def reference(self, model_name, model_type):
        
        pass


class ClassifierFunction(object):

    def __init__(self):
        super(ClassifierFunction, self).__init__(Function)
