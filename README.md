# Official OpenController Repo
The OpenController Mini is an open-source, arduino-based controller. I created it as a practice project for electronics, Python and 3D Printing. And also because I wanted to play Blasphemous with it.
You can replicate this project, but I would recommend 3D printing and Python knowledge, as I will not be holding your hand beyond the basics, even though everything is very self-explanatory. Keep in mind that it is a retro-style controller, with only a joystick and four buttons, so it is only ideal for 2D games.

![OCM VIZ](https://github.com/user-attachments/assets/c6f58a39-a297-48e4-ac0e-a1a6726f4c17)

## The Code
The Arduino listens to inputs from the buttons and the joystick and converts them to serial data using the .ino file. Python is then used to read the serial data via wired connection and pydirectinput is used to simulate the keystrokes. I have provided a basic customtkinter interface that can be used to change the key inputs you want to simulate. The keys to be simulated are saved in a .JSON file, so you do not have to worry about updating them every time.

![code-gif](https://github.com/user-attachments/assets/c3b974bd-2fd5-4795-842a-edce821fcb64)

## The Casing
I have designed the casing to require no glue or screws; it all snaps together. All you have to is print each part out, and then put it all together. They fit nicely so unless you have an IQ of an orangutang you should have no issues with this part. There are some parts of the print (TopJoystick, BottomButtons) where there is no flat surface to print it on. I recommend cutting the model in half (I use PrusaSlicer, which has this built-in), printing these models on the flat cut, and then gluing them back together.

## Circuit Wiring & Components

**My build requires the following components:**

1x Arduino Uno, 1x PS2 Joystick, 1x Mini Breadboard, 6x M-F Jumper Wires, 5x M-M Jumper Wires, 4x [Large Button.](https://dratek.cz/arduino/51540-sada-25-tlacitek-s-klobouckem-pro-arduino.html?gad_source=1&gclid=Cj0KCQjwgrO4BhC2ARIsAKQ7zUml_egRMIRf2p1JnSM8FwFwj0xu_ihA7Mek4BJJZqU5DG4Dg1_uwK4aAiw_EALw_wcB)

The circuit wiring is very simple; it is as simple as connecting the correct pins on the joystick side and only requires a very simple circuit on the buttons side. Here are closer-up images of the [joystick side](https://ibb.co/fYb3rfb) and the [button side.](https://ibb.co/fFZ69Yt)

![20241014_093256](https://github.com/user-attachments/assets/a2cb2cf1-75ce-4f66-b78b-7ce3f68d77d4)

If you have any urgent questions, please feel free to reach out to me.

Happy building!

~Adam
