import os
import json
from funcs import basicFunctionUtil
import time
import random
import pynput
from pynput.keyboard import Key, Controller
import sys #just to have the program kill itself if it loads weird
import threading
import os

kb = Controller() # <--this guy is wallace's fingies. we can control his fingies now
options = None
profile = None

def tryLoneInput(profileinput):
        currentKey = profileinput[0]
        percentToHit = profileinput[1]
        minHoldTime = profileinput[2]
        maxHoldTime = profileinput[3]


        if int(percentToHit) >= random.randint(0, 100):

            def realPress():
                kb.press(currentKey)
                #sleep for a random amount between minhold and maxhold
                time.sleep(random.uniform(minHoldTime, maxHoldTime))
                kb.release(currentKey)

            #god this is so much nicer than asyncio. it's still confusing but i think we're just essentially giving the script an extra arm to press a key with for every time this hits instead of managing everything with one arm
                        #daemon seems to just mean "if you close the program it stops"
            pressThread = threading.Thread(target=realPress, daemon=True)
            #start
            pressThread.start()


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


#checks switch
def pressKillSwitchChecker(pressedKey):
     if pressedKey == pynput.keyboard.Key.esc:
          #i am told that sys.exit() will just kill the thread. i dunno if that's true but no skin off my back to do os._exit(0) instead which seems to otherwise do the same thing
          os._exit(0)

#whenever a button presses, the executioner is watching
executioner = pynput.keyboard.Listener(on_press=pressKillSwitchChecker)
executioner.daemon = True
executioner.start()

cycle = 0

while True:
    cycle += 1
    if options["debug"]:
        print(f"Currently on cycle {str(cycle)}")
        
    for profKey in profile.values():
        tryLoneInput(profKey)

    #time.sleep determinable in options.json
    if not options["altWaitMethodVariableFromAverage"]:
        timeToWait(random.uniform(options["minWaitTime"], options["maxWaitTime"]))
    else:
        timeToWait = options["altAverageWaitTime"] + random.uniform(options["altVariance"] * -1, options["altVariance"])
        
    time.sleep(timeToWait)
    

