import json
import os


def open_config(keyword):
    try:
        with open(os.path.join(os.path.dirname(__file__), f'../data/config/{keyword}.json'), "r") as f:
            configJson = json.load(f)
            print("GOOD in open_config in config_utils.py")
            print(type(configJson))
        return configJson
    except Exception as e:
        print(f"Error in open_config: {e}")


def open_config_file(media):
    try:
        with open(os.path.join(os.path.dirname(__file__), f'../data/config/{media}.json'), "r") as f:
            configJson = json.load(f)
            print("GOOD in open_config_file in config_utils.py")
            print(type(configJson))
        return configJson
    except Exception as e:
        print(f"Error in open_config_file: {e}")


def get_json_file(*args):
    try:
        if any(keyword in args for keyword in ["url", "credentials", "pdf"]):
            print("GOOD in first if : keyword", args[0])
            configJson = open_config("config")
            return configJson

        elif any(media in args for media in ["lefigaro", "lacroix", "liberation"]):
            print("GOOD in second if : media", args[0])
            configJson = open_config_file(args[0])
            return configJson

        else:
            print("Error while getting config file")
            return
    except Exception as e:
        print(f"Error in get_json_file: {e}")
