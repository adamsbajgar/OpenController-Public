import json
import os

# This script saves and holds the control input data.
FilePath = "controls.json"

outputButtons = ["k", "j", "shift", "space"]

outputJoystick = ["w","a","s","d"]

# Updates script with up-to-date controls.
def fetchControls():
    if os.path.exists(FilePath):
        with open("controls.json","r") as file:
            buttonControls = json.load(file)
            for counter, (key, value) in enumerate(buttonControls.items()):
                if counter < 4:
                    outputButtons[counter] = value
                else:
                    outputJoystick[counter - 4] = value
    else:
        saveControls()

# Saves the controls to the .json file.
def saveControls():
    with open(FilePath, "w") as file:
        controls = {
            "blue": outputButtons[0],
            "yellow": outputButtons[1],
            "red": outputButtons[2],
            "white": outputButtons[3],
            "up": outputJoystick[0],
            "left": outputJoystick[1],
            "down": outputJoystick[2],
            "right": outputJoystick[3]
        }
        json.dump(controls, file, indent=4)
