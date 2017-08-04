#include <Servo.h> // Include servo library
Servo servoLeft; // Declare left servo signal
Servo servoRight; // Declare right servo signal
int direction = 1700;

void setup() // Built in initialization block
{
  Serial.begin(9600);
  servoLeft.attach(13); // Attach left signal to pin 13
  servoRight.attach(12); // Attach right signal to pin 12
}

void loop() // Main loop auto-repeats
{ // Empty, nothing needs repeating
  /*
  String data = Serial.readString();
  Serial.print("Data: ");
  Serial.println(data);
  */
  char c;
  if (Serial.available()) {
    c = Serial.read();
    if (c == 'b') {
      if (direction == 1700) {
        direction = 1300;
      } else {
        direction = 1700;
      }
      servoLeft.writeMicroseconds(direction); // 1.7 ms -> counterclockwise
      servoRight.writeMicroseconds(direction); // 1.3 ms -> clockwise
    }
  }
}
