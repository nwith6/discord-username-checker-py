import json


# Variables
default_config = {
    "mode": "lds",
    "delay": 20,
    "end_on_available": False,

    "username": None,
    "length": 10,
    "letters": "abcdefghijklmnopqrstuvwxyz",
    "digits": "0123456789",
    "specials": "_."
}


# Functions
def get_cache() -> dict:
    try:
        with open("username_cache.json", "rt") as file:
            return json.load(file)
    except FileNotFoundError:
        with open("username_cache.json", "wt") as file:
            json.dump({"available": [], "unavailable": []}, file, indent=4)
            return {"available": [], "unavailable": []}


def update_cache(type: str, username: str) -> dict | bool:
    updated_data = None
    with open("username_cache.json", "r+") as file:
        data = json.load(file)
        data[type].append(username); updated_data = data

        file.seek(0); json.dump(data, file, indent=4)

    if updated_data:
        return updated_data
    return False


def get_config() -> dict:
    try:
        with open("config.json", "rt") as file:
            return json.load(file)
    except FileNotFoundError:
        with open("config.json", "wt") as file:
            json.dump(default_config, file, indent=4)
            return default_config
