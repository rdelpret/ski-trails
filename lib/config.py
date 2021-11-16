import os
import yaml


def get_config():
    '''
    helper func to parse configfile
    '''

    # TODO add some safety here
    trails_dir = os.path.dirname(
        os.path.realpath(__file__)) + "/../config.yaml"

    if os.environ.get("TRAILS_CONFIG"):
        trails_dir = os.environ.get("TRAILS_CONFIG")

    with open(trails_dir, "r") as f:
        config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return config
