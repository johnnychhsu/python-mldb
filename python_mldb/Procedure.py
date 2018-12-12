# @Author: Johnny Hsu
# @Date: 2018-12-09
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-09
# @File Name:          Procedure.py
from sklearn.ensemble import RandomForestClassifier

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

    def __init__(self, name, description):
        super(ClassifierProcedure, self).__init__()
        self.name = name
        self.description = description

    def train(self, dataset_name, path, **kwargs):
        pass


class RFClassifierProcedure(ClassifierProcedure):

    def __init__(self, name, description):
        super(RFClassifierProcedure, self).__init__(name, description)

    def train(self, dataset_name, path, **kwargs):
        self._train(dataset_name, path, **kwargs)

    def _train(self, dataset_name, path, **kwargs):
        data = self.dataset.load_from_database(dataset_name)
        y = data[['label']].values()
        x = data.drop(labels=['label'], axis='columns').values()

        clf = RandomForestClassifier(n_estimators=100,
                                     max_depth=2,
                                     random_state=0,
                                     **kwargs)

        print("Start training random forest classifier with dataset {}.".format(dataset_name))
        clf.fit(x, y)

        self._save_to_db(clf, path)

    def _save_file(self, dataset_name, clf, path):
        abs_path = os.path.abspath(path)
        saved_name = self.name + '_' + dataset_name
        try:
            with open(os.path.join(abs_path, saved_name)) as f:
                pickle.dump(clf, f)
        except IOError as err:
            print(err)

    def _save_to_db(self, dataset_name, clf, path):
        self._save_file(dataset_name, clf, path)

