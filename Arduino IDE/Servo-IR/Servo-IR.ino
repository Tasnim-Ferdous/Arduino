#include <Servo.h>

Servo s;
int ir = 8;
int servo = 9;
int swh = 90;
int swl = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  s.attach(servo);
  pinMode(ir, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(ir)==LOW) {
    s.write(swh);
    delay(50);
  }
  else {
    s.write(swl);
    delay(50);
  }
}
