import json
import os



def open_config(param):
    with open(os.path.join(os.path.dirname(__file__), f'../../data/config/{param}.json'), "r") as f:
        configJson = json.load(f)

    return configJson


def open_config_file(param):
    with open(os.path.join(os.path.dirname(__file__), f'../../data/config/{param}.json'), "r") as f:
        configJson = json.load(f)

    return configJson


def get_config_file(*args):
    if any(keyword in args for keyword in ["url", "credentials", "pdf"]):
        print("GOOD in first if")
        # configJson = open_config("config")
        # return configJson

    elif any(media in args for media in ["lefigaro", "lacroix", "liberation"]):
        # configJson = open_config_file(args[0])
        print("GOOD in second if")
        # return configJson

    else:
        print("Error while getting config file")
        return

