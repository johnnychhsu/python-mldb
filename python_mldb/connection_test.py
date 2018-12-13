from python_mldb.Connector import Connector
from python_mldb.Dealer import Dealer
from python_mldb.utils import _load_config

import os


def test_connector():

    print ("Connector test start ...")

    path = os.path.abspath('./')

    config = _load_config(os.path.join(path, 'config_file/config.yaml'))

    connector = Connector(config['password'])
    flag = connector.connect()

    if flag:
        print ("Connector Test Pass!")
    else:
        print ("Connector Test Fail")


def test_dealer():

    print ("Dealer test start ...")

    dealer = Dealer('config_file/config.yaml')


def run_test():
    test_connector()
    test_dealer()


if __name__ == '__main__':
    run_test()
