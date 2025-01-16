import json


# Variables
default_config = {
    "username_regex": "[0-9a-z_.]{15}",
    "delay": 20,
    "pause_execution_if_available": False,
    "proccess_cached_usernames": True
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


# def update_cache(type: str, username: str) -> dict | bool:
#     updated_data = None
#     with open("username_cache.json", "r+") as file:
#         data = json.load(file)
#         data[type].append(username); updated_data = data

#         file.seek(0); json.dump(data, file, indent=4)

#     return updated_data


def cache_append(type: str, username: str) -> dict | bool:
    updated_data = None
    with open("username_cache.json", "r+") as file:
        data = json.load(file)
        data[type].append(username); updated_data = data

        file.seek(0); json.dump(data, file, indent=4)

    return updated_data


def cache_remove(type: str, username: str) -> dict | bool:
    updated_data = None
    with open("username_cache.json", "r+") as file:
        data = json.load(file)
        data[type].remove(username); updated_data = data

        file.seek(0); json.dump(data, file, indent=4)

    return updated_data


def get_config() -> dict:
    try:
        with open("config.json", "rt") as file:
            return json.load(file)
    except FileNotFoundError:
        with open("config.json", "wt") as file:
            json.dump(default_config, file, indent=4)
            return default_config
