import os
import time
import modules.json_utils as jutils
import modules.username_utils as uutils

from colorama import Fore, init


# Variables #
fores = {
    "tag": Fore.RED,
    "time": Fore.YELLOW,
    "available": Fore.GREEN,
    "unavailable": Fore.RED
}
tag = """ █     █░ ██▓ ██ ▄█▀ ██▓    ██▓     ▒█████   ██▓    
▓█░ █ ░█░▓██▒ ██▄█▒ ▓██▒   ▓██▒    ▒██▒  ██▒▓██▒    
▒█░ █ ░█ ▒██▒▓███▄░ ▒██▒   ▒██░    ▒██░  ██▒▒██░    
░█░ █ ░█ ░██░▓██ █▄ ░██░   ▒██░    ▒██   ██░▒██░    
░░██▒██▓ ░██░▒██▒ █▄░██░   ░██████▒░ ████▓▒░░██████▒
░ ▓░▒ ▒  ░▓  ▒ ▒▒ ▓▒░▓     ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▓  ░
  ▒ ░ ░   ▒ ░░ ░▒ ▒░ ▒ ░   ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░ ▒  ░
  ░   ░   ▒ ░░ ░░ ░  ▒ ░     ░ ░   ░ ░ ░ ▒    ░ ░   
    ░     ░  ░  ░    ░         ░  ░    ░ ░      ░  ░
                                                    """


# Functions #
def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    

def main():
    init(autoreset=True); cls()
    print("\n" + fores["tag"] + tag)

    cache = jutils.get_cache()
    config = jutils.get_config()
    characters = uutils.get_characters_string(config)

    while True:
        username = None
        if config["mode"] == "specific":
            username = characters
        else:
            username = uutils.generate_random_username(uutils.get_characters_string(config), config["length"])

            if config["continue_if_cached"] and (username in cache["available"] or username in cache["unavailable"]):
                continue

        response = uutils.discord_username_availability(username)
        type = response["available"] and "available" or "unavailable"
        cache[type].append(username); jutils.update_cache(type, username)

        t = fores["time"] + f"[{time.strftime('%d/%m/%Y %H:%M:%S')}] "
        print(t + fores[type] + f"{username} {response['message']}")
        if config["end_on_available"] and response["available"]:
            break

        time.sleep(config["delay"])


# Main #
if __name__ == "__main__":
    main()
