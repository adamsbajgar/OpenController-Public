const int buttonPins[] = {8, 9, 10, 11};
const char buttonLabels[] = {'b', 'y', 'r', 'w'};
const int numButtons = 4;

const int analogueX = A0, analogueY = A1;

int buttonStates[numButtons] = {0, 0, 0, 0};

void setup() {
  for (int i = 0; i < numButtons; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
  pinMode(analogueX, INPUT);
  pinMode(analogueY, INPUT);
  Serial.begin(9600);
}

void loop() {
  for (int i = 0; i < numButtons; i++) {
    buttonStates[i] = digitalRead(buttonPins[i]);
    if (buttonStates[i] == LOW) {
      Serial.print(buttonLabels[i]);
    }
  }

  int x = analogRead(analogueX) - 512;
  int y = analogRead(analogueY) - 512;
  Serial.println(" ," + String(x) + "&" + String(y));

  delay(50);
}
