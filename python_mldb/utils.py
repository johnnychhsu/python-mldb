import yaml


def _load_config():
    with open("config_file/config.yaml", 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as err:
            print (err)
    return config
