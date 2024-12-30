import json
import random
import requests


# Variables
_register_data = {
    "email": "PFxFXqzv6V@5g62FU4hj9.coom",
    "username": None,
    "global_name": "QLyjCjY5rf",
    "password": "P5VlXlzH2Th",
    "invite": None,
    "consent": True,
    "date_of_birth": "2000-01-01"
}
_headers = {"Content-Type": "application/json"}
_edited_messages = {
    "USERNAME_ALREADY_TAKEN": "is unavailable.",
    "BASE_TYPE_BAD_LENGTH": "is too short/long.",
    "CUSTOM_TYPE_SUCCESS": "is available."
}


# Functions
def discord_username_availability(username: str) -> dict:
    _register_data["username"] = username
    response = requests.post("https://discord.com/api/v9/auth/register", data=json.dumps(_register_data), headers=_headers).json()

    if response.get("message") and response["code"] == 50035:
        return {"available": False, "message": _edited_messages[response["errors"]["username"]["_errors"][0]["code"]]}
    return {"available": True, "message": _edited_messages["CUSTOM_TYPE_SUCCESS"]}


def generate_random_username(characters: str, length: int) -> str:
    return "".join(random.choices(characters, k=length))


def get_characters_string(config: dict) -> str:
    if config["mode"] == "specific":
        if config["username"] == None:
            raise ValueError("Mode is set to 'specific' but username is not set in the config file.")
        return config["username"]
    else:
        return ''.join(config[set_type] for set_type in ["letters", "digits", "specials"] if set_type[0] in config["mode"])
