import yaml

from Connector import Connector


with open("config_file/config.yaml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as err:
        print (err)


connector = Connector(config['password'])
connector.connect()

print ("Pass Test!")


