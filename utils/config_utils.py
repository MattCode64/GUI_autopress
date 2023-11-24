import json
import os


def open_config():
    """
    Open the config file

    :return:
    """
    try:
        with open(os.path.join(os.path.dirname(__file__), f'../data/config/config.json'), "r") as f:
            configJson = json.load(f)
        return configJson

    except Exception as e:
        print(f"Error in open_config: {e}")


def open_config_file(media):
    """
    Open the config file for a specific media

    :param media:
    :return:
    """
    try:
        with open(os.path.join(os.path.dirname(__file__), f'../data/config/{media}.json'), "r") as f:
            configJson = json.load(f)
        return configJson

    except Exception as e:
        print(f"Error in open_config_file: {e}")


def get_json_file(*args):
    """
    Get the json file

    :param args:
    :return:
    """
    try:
        if any(keyword in args for keyword in ["url", "credentials", "pdf"]):
            configJson = open_config()
            return configJson[args[0]]

        elif any(media in args for media in ["lefigaro", "lacroix", "liberation"]):
            configJson = open_config_file(args[0])
            return configJson

        else:
            print("Error while getting config file")
            return

    except Exception as e:
        print(f"Error in get_json_file: {e}")
