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

    def show_model(self, model_table_name):
        pass

    def reference(self, model_name, time, data_table_name, test_data_table, feature_col):
        pass


class ClassifierFunction(Function):

    def __init__(self, query_handler, dataset, model_name):
        super(ClassifierFunction, self).__init__(query_handler, dataset)
        self.model_name = model_name

    def show_model(self, model_table_name):
        self._show_model(model_table_name)

    def _show_model(self, model_table_name):
        if _check_table_not_exist(self.query_handler, model_table_name):
            print("Table not exists!")
        else:
            query = "SELECT * FROM {}".format(model_table_name)
            self.query_handler.flush_cursor()
            _result = self.query_handler.run_query(query)
            for result in _result:
                print(result)


class RFClassifierFunction(ClassifierFunction):

    def __init__(self, query_handler, dataset, model_name, model_table_name):
        super(RFClassifierFunction, self).__init__(query_handler, dataset, model_name)
        self.table_name = model_table_name

    def reference(self, model_name, time, data_table_name, test_data_table, feature_col):
        if _check_table_not_exist(self.query_handler, self.table_name):
            print("Table not exists!")
        else:
            query_1 = "SELECT model FROM {} WHERE name='{}' "
            query_2 = "AND savetime='{}' AND dataset='{}'"
            query = query_1 + query_2
            query = query.format(self.table_name, model_name, time, data_table_name)

            self.query_handler.flush_cursor()
            _db_result = self.query_handler.run_query(query)

            _model_bytes = ""
            # The return result is tuple
            for result in _db_result:
                _model_bytes = result[0]

            try:
                # with open(_model_path, 'rb') as f:
                clf = pickle.loads(_model_bytes.encode())
            except IOError as err:
                print('IOError({}): {}'.format(err.errno, err.strerror))
                return

            test_data = self.dataset.load_from_database(test_data_table)
            test_feature = test_data[feature_col].values
            _ans = clf.predict(test_feature)
            print(_ans)


class SVClassifierFunction(ClassifierFunction):

    def __init__(self, query_handler, dataset, model_name, model_table_name):
        super(SVClassifierFunction, self).__init__(query_handler, dataset, model_name)
        self.table_name = model_table_name

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


class CustomizedClassifierFunction(ClassifierFunction):

    def __init__(self, query_handler, dataset, model_name, model_table_name, reference_op, load_op):
        super(CustomizedClassifierFunction, self).__init__(query_handler, dataset, model_name)
        self.model_table_name = model_table_name
        self.reference_op = reference_op
        self.load_op = load_op

    def reference(self, model_name, time, data_table_name, test_data_table, feature_col):
        if _check_table_not_exist(self.query_handler, self.model_table_name):
            print("Table not exists!")
        else:
            query_1 = "SELECT model_path FROM {} WHERE name='{}' "
            query_2 = "AND savetime='{}' AND dataset='{}'"
            query = query_1 + query_2
            query = query.format(self.model_table_name, model_name, time, data_table_name)

            # load testing data first because the it is the same for all type of model
            test_data = self.dataset.load_from_database(test_data_table)
            test_feature = test_data[feature_col].values

            self.query_handler.flush_cursor()
            _db_result = self.query_handler.run_query(query)

            _model_path = ''
            # The return result is tuple
            for result in _db_result:
                _model_path = result[0]

            if self.load_op == 'pickle':
                try:
                    with open(_model_path, 'rb') as f:
                        _model = pickle.load(f)
                except IOError as err:
                    print('IOError({}): {}'.format(err.errno, err.strerror))
                    return

                _ans = _model.predict(test_feature)
            else:
                if callable(self.load_op):
                    _model = self.load_op(_model_path)
                    _ans = _model.predict(test_feature, verbose=1)
                else:
                    print("Currently not support this type of model, we will extend it ASAP.")
                    return

            print(_ans)
