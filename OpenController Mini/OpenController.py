import serial
import pydirectinput
import Frontend
import subprocess
import ControllerData
import threading
import time

# "backend" functionality, connects to the controller, simulates keystrokes, etc.
def controllerRun():
    ControllerData.fetchControls()
    
    potentialPorts = ['COM{}'.format(i) for i in range(1, 11)]
    arduino = None

	# Loops through ports, tries to find an arudino connection.
    for port in potentialPorts:
        try:
            arduino = serial.Serial(port, 9600, timeout=.1)
            if arduino.is_open:
                Frontend.triggerConnected(True)
                print(f"Connected to Arduino on {port}")
                break
            else:
                arduino.close()
                arduino = None
                Frontend.triggerConnected(False)
        except serial.SerialException:
            print(f"Could not open port {port}")

    if arduino is None:
        print("Arduino is not connected on any port.")
        Frontend.triggerConnected(False)
        return

    # Input and corresponding output buttons, to be changed via UI by user.
    inputButtons = ["b", "y", "r", "w"]

    # List same length as input buttons, all are false at the start.
    previousButtonState = [False] * len(inputButtons)

    # Needed to avoid repeated keystrokes down by joystick.
    # Wrote it out to make it more readable.
    joystickLastState = {
        "lastLeft" : "down",
        "lastRight" : "down",
        "lastDown" : "down",
        "lastUp" : "down"
    }

    pydirectinput.PAUSE = 0

    # Function that triggers key press or release based on state.
    def triggerKeyButton(key, downBool):
        if downBool:
            pydirectinput.keyDown(key)
        else:
            pydirectinput.keyUp(key)

    def triggerKeyJoystick(key, downBool, direction):
        if downBool:
            pydirectinput.keyDown(key)
            joystickLastState[direction] = "up"
        else:
            if (joystickLastState[direction] != "down"):
                pydirectinput.keyUp(key)
                joystickLastState[direction] = "down"


    # Main loop which continuously reads data and triggers actions
    while True:
        # Decoded arduino data.
        data = arduino.readline().decode('utf-8').strip().split(",")

        # if there are at least 2 elements in data (button data and joystick data)
        if len(data) >= 2:
            dataButtons = data[0]
            dataJoystick = data[1]
            for i, button in enumerate(inputButtons):  # Looping through keeping track of index and button value at the same time.
                isPressed = button in dataButtons  # Check if button from the inputButton list is pressed in the gathered button data.
                if isPressed != previousButtonState[i]:  # If it does not match the previous button state, trigger a change.
                    triggerKeyButton(ControllerData.outputButtons[i], isPressed)
                    previousButtonState[i] = isPressed

            dataJoystick = dataJoystick.split("&")
            dataX = float(dataJoystick[0])
            dataY = float(dataJoystick[1])

            # Check joystick data, update accordingly.
            if dataY < -50: # left.
                triggerKeyJoystick(ControllerData.outputJoystick[1], True, "lastLeft")
            else:
                triggerKeyJoystick(ControllerData.outputJoystick[1], False, "lastLeft")
            if dataY > 50: # right.
                triggerKeyJoystick(ControllerData.outputJoystick[3], True, "lastRight")
            else:
                triggerKeyJoystick(ControllerData.outputJoystick[3], False, "lastRight")
            if dataX < -50: #down.
                triggerKeyJoystick(ControllerData.outputJoystick[2], True, "lastDown")
            else:
                triggerKeyJoystick(ControllerData.outputJoystick[2], False, "lastDown")
            if dataX > 50: # up.
                triggerKeyJoystick(ControllerData.outputJoystick[0], True, "lastUp")
            else:
                triggerKeyJoystick(ControllerData.outputJoystick[0], False, "lastUp")

# Uses a different thread, guarantees that it does not block processing of other scripts.
backendThread = threading.Thread(target=controllerRun)
backendThread.daemon = True
backendThread.start()

Frontend.openWindow()