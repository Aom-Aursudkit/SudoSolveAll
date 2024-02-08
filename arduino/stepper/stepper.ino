const int dirpin = 2;
const int pulpin = 5;
const int enpin = 8;
boolean dir = LOW;

volatile int spr = 800;

void flip_state() {
  dir = !dir;
}

void setup() {
  Serial.begin(9600);
  pinMode(dirpin, OUTPUT);
  pinMode(pulpin, OUTPUT);
  pinMode(enpin, OUTPUT);
  digitalWrite(enpin, LOW);
  attachInterrupt(digitalPinToInterrupt(dirpin), flip_state, FALLING);  
}

void loop() {
  // if (Serial.available() > 0) {
  //   int message = Serial.read();
  //   stepperControl(message,LOW);
  // }
  // dir = LOW;
  // for (int x = 0; x < (spr / 360.0) * 360; x++) {
  //   digitalWrite(dirpin, dir);
  //   digitalWrite(pulpin, HIGH);
  //   delayMicroseconds(250);
  //   digitalWrite(pulpin, LOW);
  //   delayMicroseconds(250);
  // }
  // delay(1000);
  // dir = HIGH;
  // for (int x = 0; x < (spr / 360.0) * 360; x++) {
  //   digitalWrite(dirpin, dir);
  //   digitalWrite(pulpin, HIGH);
  //   delayMicroseconds(250);
  //   digitalWrite(pulpin, LOW);
  //   delayMicroseconds(250);
  // }
  // delay(1000);
  stepperControl(90,HIGH);
  // stepperControl(90,HIGH);
  delay(100);
}

void stepperControl(int dg,boolean y){
  dir = y;
  digitalWrite(dirpin, y);
  for (int x = 0; x < (spr / 360.0) * dg; x++) {
    digitalWrite(pulpin, HIGH);
    delayMicroseconds(200);
    digitalWrite(pulpin, LOW);
    delayMicroseconds(200);
  }
}
