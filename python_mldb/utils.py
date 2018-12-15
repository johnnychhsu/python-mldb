import yaml
from datetime import datetime


def _load_config(config_file):
    with open(config_file, 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as err:
            print (err)
    return config


def _create_database(query_handler, name):
    query = "CREATE DATABASE {};".format(name)
    query_handler.run_query(query)


def _use_database(query_handler, db_name):  
    query_handler.flush_cursor()
    query = "USE {}".format(db_name)
    query_handler.run_query(query)


def _check_db_not_existed(query_handler, name):
    query = "SHOW DATABASES;"
    _result = query_handler.run_query(query)
    for db in _result:
        if name in db:
            return False
    return True


def _create_model_table(query_handler, table_name):
    values = '(name VARCHAR(25), savetime DATETIME, dataset VARCHAR(25), model_path VARCHAR(250), ' + \
             'CONSTRAINT PK Primary Key (name, savetime, dataset))'
    query = "CREATE TABLE {} {}".format(table_name, values)
    query_handler.run_query(query)


def _check_table_not_exist(query_handler, table_name):
    query = "SHOW TABLES;"
    _result = query_handler.run_query(query)
    for table in _result:
        if table_name in table:
            return False
    return True


def _check_row_not_exist(query_handler, pk):
    query = ""


def _current_time():
    d = datetime.now().isoformat()
    return d
