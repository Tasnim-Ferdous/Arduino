int trigPin = 9;
int echoPin = 8;
float travelTime; //in microsecond
float travelDistance; //in cm
float distance; //in cm
float speed; //in cm/microsecond

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  travelTime = pulseIn(echoPin, HIGH);
  travelDistance = 0.0352*travelTime;
  distance = travelDistance/2;
  delay(50);
  Serial.print(travelTime);
  Serial.print(" ");
  Serial.println(distance);
}
