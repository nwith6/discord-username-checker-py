import os
import time
import rstr
import modules.json_utils as jutils
import modules.request_utils as rutils

from colorama import Fore, init


# Variables
fores = {
    "tag": Fore.RED,
    "error": Fore.RED,
    "time": Fore.YELLOW,
    "pause": Fore.WHITE,
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


# Functions
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

    while True:
        try:
            username = rstr.xeger(config["username_regex"])
        except:
            print(fores["tag"] + "Invalid regex pattern."); break

        if (username in cache["available"] or username in cache["unavailable"]) and not config["proccess_cached_usernames"]:
            continue

        response = rutils.discord_username_availability(username)

        type = response["available"] and "available" or "unavailable"
        if username not in cache[type]:
            cache[type].append(username); jutils.update_cache(type, username)

        t = fores["time"] + f"[{time.strftime('%d/%m/%Y %H:%M:%S')}] "
        print(t + f"{fores[type]}{username} {response['message']}")

        if config["pause_execution_if_available"] and response["available"]:
            input(f"\n{fores['pause']}Press enter to continue..."); continue
        
        time.sleep(config["delay"])


# Main
if __name__ == "__main__":
    main()
