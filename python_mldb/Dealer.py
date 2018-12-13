# @Author: Johnny Hsu
# @Date: 2018-12-12
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-12
# @File Name:          Dealer.py
from python_mldb.Connector import Connector
from python_mldb.Dataset import Dataset
from python_mldb.Procedure import Procedure
from python_mldb.Function import Function
from python_mldb.query_handler import QueryHandler
from python_mldb.utils import _load_config, _create_database, _check_db_not_existed, _use_database


class Dealer(object):

    def __init__(self, config_file):

        config = _load_config(config_file)
        host = config['host']
        user = config['name']
        password = config['password']

        self.connector = Connector(user=user,
                                   host=host,
                                   password=password)

        self.connector.connect()
        self.query_handler = QueryHandler(self.connector.mydb, self.connector.cursor)

        if _check_db_not_existed(self.query_handler, config['database']):
            _create_database(self.query_handler, config['database'])
        else:
            print ("Warning: Database {} already existed!".format(config['database']))

        _use_database(self.query_handler, config['database'])

        self.dataset = Dataset(self.query_handler)
        self.procedure = Procedure(self.query_handler, self.dataset)
        self.function = Function(self.query_handler, self.dataset)

        print ("Dealer established, service start!")
