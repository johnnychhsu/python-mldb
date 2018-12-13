import yaml


def _load_config(config_file):
    with open(config_file, 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as err:
            print (err)
    return config


def _create_database(query_handler, name):
    query = "CREATE DATABASE {}".format(name)
    query_handler.run_query(query)


def _check_db_not_existed(query_handler, name):
    query = "SHOW DATABASES;"
    _result = query_handler.run_query(query)
    for db in _result:
        if name in db:
            return False
    return True
