#include <Servo.h>

Servo s;
int servo = 9;
int sw = 90;
String cmd;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  s.attach(servo);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()==0) {

  }
  sw = Serial.readStringUntil("\r").toInt();
  s.write(sw);
  delay(50);
}
