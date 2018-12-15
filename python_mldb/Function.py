# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-09
# @File Name:          Function.py

from sklearn.ensemble import RandomForestClassifier
from python_mldb.utils import _check_table_not_exist

class Function(object):

    def __init__(self, query_handler, dataset):
        self.query_handler = query_handler
        self.dataset = dataset

    def show_model(self):
        pass

    def reference(self, model_name, model_type):
        
        pass


class ClassifierFunction(Function):

    def __init__(self, query_handler, dataset):
        super(ClassifierFunction, self).__init__(query_handler, dataset)

class RFClassifierFunction(ClassifierFunction):

    def __init__(self, query_handler, dataset):
        super(RFClassifierFunction, self).__init__(query_handler, dataset)
        self.table_name = 'RF_Model'

    def show_model(self):
        _show_model()

    def _show_model(self):
        if _check_table_not_exist(self.query_handler, self.table_name):
            print("Table not exists!")
        else:
            query = "SELECT * FROM {}".format(self.table_name)
            self.query_handler.flush_cursor()
            self.query_handler.run_query(query)
        print(query)

    def reference(self, model_name, model_type):
        
        pass
