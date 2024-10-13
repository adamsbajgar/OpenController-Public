# Official OpenController Repo
OpenController is an open-source, arduino-based controller. I created it as a practice project for electronics and Python.
You can replicate this project, but I would recommend 3D printing and Python knowledge, as I will not be holding your hand beyond the basics, even though everything is very self-explanatory. Keep in mind that it is a retro-style controller, with only a joystick and four buttons, so it is only ideal for 2D games.

![OCM VIZ](https://github.com/user-attachments/assets/c6f58a39-a297-48e4-ac0e-a1a6726f4c17)

### The Code
The Arduino listens to inputs from the buttons and the joystick and converts them to serial data using the .ino file. Python is then used to read the serial data via wired connection and pydirectinput is used to simulate the keystrokes. I have provided a basic customtkinter interface that can be used to change the key inputs you want to simulate. The keys to be simulated are saved in a .JSON file, so you do not have to worry about updating them every time.

## The Casing
I have designed the casing to require no glue or screws; it all snaps together. All you have to is print each part out, and then put it all together. They fit nicely so unless you have an IQ of an orangutang you should have no issues with this part. There are some parts of the print (TopJoystick, BottomButtons) where there is no flat surface to print it on. I recommend cutting the model in half (I use PrusaSlicer, which has this built-in), printing these models on the flat cut, and then gluing them back together.
