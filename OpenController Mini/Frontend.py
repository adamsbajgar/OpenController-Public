import customtkinter as ctk
import os
import tkinter.font as tkfont
import ControllerData

CURRENT_COLOR = "#0BA1FF"
TILTWARP_FONT = "Tilt Warp Regular"
STATUS = "Disconnected"

ctk.set_appearance_mode("dark")

#Used to open the OpenController Mini settings window.
def openOCMini():
    app = OpenControllerApp()
    app.iconbitmap("logo.ico")
    app.mainloop()

#Used to update if the controller is connected or not.
def triggerConnected(bool):
    global STATUS
    if bool:
        STATUS = "Connected"
    else:
        STATUS = "Disconnected"

# OpenController Mini Settings.
class OpenControllerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("OpenController Mini Settings")
        self.geometry("550x600")
        
        self.settings_frame = ctk.CTkFrame(self, width=450, height=550, corner_radius=15)
        self.settings_frame.pack(pady=5, padx=5, fill="both", expand=True)

        settings_label = ctk.CTkLabel(self.settings_frame, text="OpenController Mini - Settings", font=(TILTWARP_FONT, 20), text_color=CURRENT_COLOR)
        settings_label.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        description_label = ctk.CTkLabel(self.settings_frame, text="Change your OpenController configuration using the settings below.", font=(TILTWARP_FONT, 14))
        description_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        button_section_label = ctk.CTkLabel(self.settings_frame, text="Input Functions", font=(TILTWARP_FONT, 18))
        button_section_label.grid(row=2, column=0, columnspan=2, padx=20, sticky="w")

        button_section_label = ctk.CTkLabel(self.settings_frame, text="Controller Status: "+STATUS, font=(TILTWARP_FONT, 18))
        button_section_label.grid(row=16, column=0, columnspan=2, pady=(10, 5))

        update_button = ctk.CTkButton(self.settings_frame, text="Update", width=200, height=40, fg_color=CURRENT_COLOR, font=(TILTWARP_FONT, 16, "bold"), command=self.updateControls)
        update_button.grid(row=17, column=0, columnspan=2, pady=(10, 10))

        self.entries = {}

        button_labels = ["Blue Button", "Yellow Button", "Red Button", "White Button"]
        for idx, label_text in enumerate(button_labels):
            row = (idx // 2) + 3
            column = idx % 2
            self.CreateEntry(label_text, row, column, idx, "button")

        joystick_labels = ["Joystick Up", "Joystick Down", "Joystick Left", "Joystick Right"]
        for idx, label_text in enumerate(joystick_labels):
            row = (idx // 2) + 7
            column = idx % 2
            self.CreateEntry(label_text, row, column, idx, "joystick")
    
    def updateControls(self):
        for labelText, entry in self.entries.items():
            inputText = entry.get()
            if inputText != "":
                if "Button" in labelText:
                    idx = ["Blue Button", "Yellow Button", "Red Button", "White Button"].index(labelText)
                    ControllerData.outputButtons[idx] = inputText
                else:
                    idx = ["Joystick Up", "Joystick Down", "Joystick Left", "Joystick Right"].index(labelText)
                    ControllerData.outputJoystick[idx] = inputText
                ControllerData.saveControls()
    
    def CreateEntry(self, label_text, row, column, idx, section):
        entryText = ""
        offset = 0
        if (row % 2 == 0):
            offset = 1
        entry_label = ctk.CTkLabel(self.settings_frame, text=label_text, font=(TILTWARP_FONT, 14), text_color=CURRENT_COLOR)
        entry_label.grid(row=row + offset, column=column, padx=30, pady=(10, 5), sticky="w")
        if section == "button":
            entryText = ControllerData.outputButtons[idx]
        else:
            entryText = ControllerData.outputJoystick[idx]
        entry = ctk.CTkEntry(self.settings_frame, width=200, height=25, placeholder_text = entryText)
        entry.grid(row=row + 1 + offset, column=column, padx=30, pady=(5, 15), sticky="w")

        self.entries[label_text] = entry
        # Stores references to entry boxes to be later used to fetch values.

# Create the connect window, which I can implement other controller versions into later.
class OpenControllerConnectApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Settings Page")
        self.geometry("400x400")
        
        self.connect_frame = ctk.CTkFrame(self, width=350, height=350, corner_radius=15)
        self.connect_frame.pack(pady=5, padx=5, fill="both", expand=True)

        connect_label = ctk.CTkLabel(self.connect_frame, text="OpenController - Connect", font=(TILTWARP_FONT, 20), text_color=CURRENT_COLOR)
        connect_label.pack(pady=(10, 5))

        description_label = ctk.CTkLabel(self.connect_frame, text="Please connect to your OpenController.", font=(TILTWARP_FONT, 14))
        description_label.pack(pady=(0, 20))

        mini_button = ctk.CTkButton(self.connect_frame, text="OpenController Mini", width=200, height=40, fg_color=CURRENT_COLOR, font=(TILTWARP_FONT, 16), command=openOCMini)
        mini_button.pack(pady=(0, 15))

        available_button = ctk.CTkButton(self.connect_frame, text="Available", width=200, height=40, fg_color=CURRENT_COLOR, font=(TILTWARP_FONT, 16))
        available_button.pack()

def openWindow():
    app = OpenControllerConnectApp()
    app.iconbitmap("logo.ico")
    app.mainloop()