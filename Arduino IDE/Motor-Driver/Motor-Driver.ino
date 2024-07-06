//Motor A
int enA = 3;
int in1 = 4;
int in2 = 5;


void setup() {
  // put your setup code here, to run once:
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

}

void demoOne() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  analogWrite(enA, 200);

  delay(3000);

  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);

  delay(3000);

  
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);

  delay(3000);
}

void demoTwo() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);

  for (int i = 0; i < 256; i++) {
    analogWrite(enA, i);

    delay(200);
  }

  for (int i = 255; i >= 0; --i) {
    analogWrite(enA, i);

    delay(200);
  }

  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  demoOne();
  delay(1000);
  demoTwo();
  delay(1000);
}
