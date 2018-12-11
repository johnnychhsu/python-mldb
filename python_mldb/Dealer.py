# @Author: Johnny Hsu
# @Date: 2018-12-12
# @Last Modified by:   Johnny Hsu
# @Last Modified time: 2018-12-12
# @File Name:          Dealer.py
from Connector import Connector
from Dataset import Dataset
from Procedure import Procedure
from Function import Function
from query_handler import QueryHandler
from utils import _load_config


class Dealer(object):

    def __init__(self):

        config = _load_config()
        host = config['host']
        user = config['user']
        password = config['password']

        self.connector = Connector(user=user,
                                   host=host,
                                   password=password)

        self.connector.connect()

        self.query_handler = QueryHandler(self.connector, self.connector.cursor)
        self.dataset = Dataset(self.query_handler)
        self.procedure = Procedure(self.query_handler, self.dataset)
        self.function = Function(self.query_handler, self.dataset)

        print ("Dealer established, service start!")
