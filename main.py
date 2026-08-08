import os
import json
from funcs import basicFunctionUtil
import time
from pynput.keyboard import Key, Controller
import sys #just to have the program kill itself if it loads weird

kb = Controller() # <--this guy is wallace's fingies. we can control his fingies now
options = None
profile = None


try:
    options = basicFunctionUtil.loadFileAsJSON(f"./options.json")
    profile = basicFunctionUtil.loadFileAsJSON(f"./profiles/{options["profile"]}.json")

    if options["debug"]:
        print(f"Options successfully loaded.\nCurrent profile: \"{options["profile"]}\"")

    print(f"Hello. Do you want to play a Game with \"{options["name"]}\"?")
    input(f"Press Enter to continue...")

except:
    input("you broke something. press enter to close")
    sys.exit()



while True:
    print("")