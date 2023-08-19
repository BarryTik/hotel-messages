import argparse
import json

def get_args():
    """
    Argument parser for ingesting command line arguments
    :return args: Namespace object containing the command line arguments
    """
    parser = argparse.ArgumentParser("Hotel Messages")

    # Required positional arguments
    parser.add_argument(
        "company_id"
    )
    parser.add_argument(
        "guest_id"
    )

    # Optional flag arguments
    parser.add_argument(
        "--template", "-t",
        dest="template"
    )
    parser.add_argument(
        "--message", "-m",
        dest="user_message"
    )

    args = parser.parse_args()
    return args

def get_json(json_path):
    """
    Function for getting input JSONs
    :param json_path: String, path to a .json file
    :return: Dictionary, the contents of the file at json_path
    """
    with open(json_path, "r") as infile:
        return json.load(infile)

