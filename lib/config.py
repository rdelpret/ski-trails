import os
import yaml

def get_config():
    '''
    helper func to parse configfile
    '''

    #TODO add some safety here
    trails_dir = os.path.dirname(os.path.realpath(__file__))
    
    with open(trails_dir + "/../config.yaml", "r") as f:
      config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return config