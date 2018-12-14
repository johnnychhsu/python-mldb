# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-09
# @File Name:          Procedure.py
from sklearn.ensemble import RandomForestClassifier
from python_mldb.utils import _current_time, _create_model_table, _check_table_not_exist
import numpy as np

import os
import pickle


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

    def __init__(self, query_handler, dataset, model_name):
        super(ClassifierProcedure, self).__init__(query_handler, dataset)
        self.model_name = model_name

    def train(self, dataset_name, label_col, feature_col, saved_model_path):
        pass


class RFClassifierProcedure(ClassifierProcedure):

    def __init__(self, query_handler, dataset, model_name):
        super(RFClassifierProcedure, self).__init__(query_handler, dataset, model_name)
        self.table_name = 'RF_Model'

    def train(self, data_table_name, label_col, feature_col, saved_model_path='', **kwargs):
        self._train(data_table_name, label_col, feature_col, saved_model_path, **kwargs)

    def _train(self, data_table_name, label_col, feature_col, saved_model_path, **kwargs):
        data = self.dataset.load_from_database(data_table_name)
        y = data[label_col].values
        x = data[feature_col].values

        y = np.ravel(y)

        clf = RandomForestClassifier(n_estimators=100,
                                     max_depth=2,
                                     random_state=0,
                                     verbose=1,
                                     **kwargs)

        print("Start training random forest classifier with dataset {}.".format(data_table_name))
        clf.fit(x, y)

        self._save_to_db(clf, data_table_name)

    def _save_to_db(self, clf, data_table_name):
        if _check_table_not_exist(self.query_handler, self.table_name):
            self.query_handler.flush_cursor()
            _create_model_table(self.query_handler, self.table_name)
        else:
            print("Table already existed!")

        current_time = _current_time()
        saved_model_name = current_time + '_' + data_table_name + '_' + self.model_name + '.pickle'

        root_path = os.path.abspath('./../saved_model/')
        saved_model_path = os.path.join(root_path, saved_model_name)
        with open(saved_model_path, 'wb') as f:
            pickle.dump(clf, f)

        current_time = current_time.replace("T", ' ')

        query = "INSERT INTO {} VALUES ('{}','{}','{}','{}')".format(self.table_name,
                                                                     self.model_name,
                                                                     current_time,
                                                                     data_table_name,
                                                                     saved_model_path)
        self.query_handler.flush_cursor()
        self.query_handler.run_query(query)

        print(query)

        print("Trained model is saved in database {}, table {}.".format(self.query_handler.connector.database, self.table_name))

