from Connector import Connector
from Dealer import Dealer
from utils import _load_config


def test_connector():

    print ("Connector test start ...")

    config = _load_config()

    connector = Connector(config['password'])
    flag = connector.connect()

    if flag:
        print ("Connector Test Pass!")
    else:
        print ("Connector Test Fail")


def test_dealer():

    print ("Dealer test start ...")

    dealer = Dealer()


def run_test():
    test_connector()
    test_dealer()


if __name__ == '__main__':
    run_test()
