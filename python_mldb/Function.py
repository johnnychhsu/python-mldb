# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-09
# @File Name:          Function.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from python_mldb.utils import _check_table_not_exist

import pickle


class Function(object):

    def __init__(self, query_handler, dataset):
        self.query_handler = query_handler
        self.dataset = dataset

    def show_model(self):
        pass

    def reference(self, model_name, time, data_table_name, test_data_table, feature_col):
        pass


class ClassifierFunction(Function):

    def __init__(self, query_handler, dataset, model_name):
        super(ClassifierFunction, self).__init__(query_handler, dataset)
        self.model_name = model_name


class RFClassifierFunction(ClassifierFunction):

    def __init__(self, query_handler, dataset, model_name):
        super(RFClassifierFunction, self).__init__(query_handler, dataset, model_name)
        self.table_name = 'RF_Model'

    def show_model(self):
        self._show_model()

    def _show_model(self):
        if _check_table_not_exist(self.query_handler, self.table_name):
            print("Table not exists!")
        else:
            query = "SELECT * FROM {}".format(self.table_name)
            self.query_handler.flush_cursor()
            _result = self.query_handler.run_query(query)
            for result in _result:
                print(result)

    def reference(self, model_name, time, data_table_name, test_data_table, feature_col):
        if _check_table_not_exist(self.query_handler, self.table_name):
            print("Table not exists!")
        else:
            query_1 = "SELECT model_path FROM {} WHERE name='{}' "
            query_2 = "AND savetime='{}' AND dataset='{}'"
            query = query_1 + query_2
            query = query.format(self.table_name, model_name, time, data_table_name)

            self.query_handler.flush_cursor()
            _db_result = self.query_handler.run_query(query)

            _model_path = ''
            # The return result is tuple
            for result in _db_result:
                _model_path = result[0]

            try:
                with open(_model_path, 'rb') as f:
                    clf = pickle.load(f)
            except IOError as err:
                print('IOError({}): {}'.format(err.errno, err.strerror))
                return

            test_data = self.dataset.load_from_database(test_data_table)
            test_feature = test_data[feature_col].values
            _ans = clf.predict(test_feature)
            print(_ans)


class SVClassifierFunction(ClassifierFunction):

    def __init__(self, query_handler, dataset, model_name):
        super(SVClassifierFunction, self).__init__(query_handler, dataset, model_name)
        self.table_name = 'SV_Model'

    def show_model(self):
        self._show_model()

    def _show_model(self):
        if _check_table_not_exist(self.query_handler, self.table_name):
            print("Table not exists!")
        else:
            query = "SELECT * FROM {}".format(self.table_name)
            self.query_handler.flush_cursor()
            _result = self.query_handler.run_query(query)
            for result in _result:
                print(result)

    def reference(self, model_name, time, data_table_name, test_data_table, feature_col):
        if _check_table_not_exist(self.query_handler, self.table_name):
            print("Table not exists!")
        else:
            query_1 = "SELECT model_path FROM {} WHERE name='{}' "
            query_2 = "AND savetime='{}' AND dataset='{}'"
            query = query_1 + query_2
            query = query.format(self.table_name, model_name, time, data_table_name)

            self.query_handler.flush_cursor()
            _db_result = self.query_handler.run_query(query)

            _model_path = ''
            # The return result is tuple
            for result in _db_result:
                _model_path = result[0]

            try:
                with open(_model_path, 'rb') as f:
                    clf = pickle.load(f)
            except IOError as err:
                print('IOError({}): {}'.format(err.errno, err.strerror))
                return

            test_data = self.dataset.load_from_database(test_data_table)
            test_feature = test_data[feature_col].values
            _ans = clf.predict(test_feature)
            print(_ans)

