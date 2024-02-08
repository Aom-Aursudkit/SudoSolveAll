#define m1en 5
#define m1a 7
#define m1b 6

#define LPD3806 400

volatile int32_t temp, counter;
int PinALastState = LOW;
int pinAState = LOW;

#define maxTurn 10
float turn;

long d;
int i;
float P = 0;
float I = 0;
float D = 0;
float PID;
float error, errorr;
float Kp = 1.2;
float Ki = 0.35;
float Kd = 10 ;
float degree = -1;
String input = "";
float adjust = 1.0023;

void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(m1en, OUTPUT);
  pinMode(m1a, OUTPUT);
  pinMode(m1b, OUTPUT);
  pinMode(12, OUTPUT);

  counter = 0;
  attachInterrupt(0, Encoder, CHANGE);
  attachInterrupt(1, Encoder, CHANGE);
  while (1) {
    if (Serial.available() > 0) {
      input = Serial.readString();
      degree = pow(input.toFloat(),adjust);
    }
    if (degree >= 0){
      break;
    }
  }

  while (digitalRead(13) == 1) {
    go(-100);
  }
  // go(0);
  // delay(100);
  // go(100);
  // delay(50);
  go(0);
  delay(300);
  counter = 0;
}

void loop() {
  // if (counter != temp) {
  //   Serial.print("Encoder count : ");
  //   Serial.println(counter);
  //   Serial.print("     ");

  //   turn = (float)counter / LPD3806;

  //   Serial.print(turn, 3);  //นับรอบที่ encoder
  //   Serial.println(" turn");
  //   temp = counter;
  // }
  ///////////////////////////
  if (Serial.available() > 0) {
    input = Serial.readString();
    degree = pow(input.toFloat(),adjust);
  }
  ///////////////////////////
  // degree = 90;
  readd(2.222223 * degree);
  pidd();
  float ms = -PID;
  go(ms);
  if (error >= -1 && error <= 1) {
    go(0);
  } else {
    d = millis();
    digitalWrite(12, LOW);
  }
  if (millis() - d > 500 && error >= -1 && error <= 1) {
    digitalWrite(12, HIGH);
    go(0);
    delay(1500);
    while (digitalRead(13) == 1) {
      digitalWrite(12, LOW);
      go(-100);
    }
    // go(0);
    // delay(100);
    // go(100);
    // delay(50);
    go(0);
    delay(300);
    counter = 0;
  }
  //////////////////////////
  // digitalWrite(12, HIGH);
  // go(100);
  // if (digitalRead(13) == 0){
  //   counter = 0;
  // }
}

void Encoder() {
  pinAState = digitalRead(2);
  if (pinAState != PinALastState) {
    if (digitalRead(3) != pinAState) {
      counter++;
    } else {
      counter--;
    }
    // Serial.println(Counter);
  }
  PinALastState = pinAState;
}

// void EncoderA() {
//   if (digitalRead(3) == LOW) counter++;
//   else counter--;
// }

// void EncoderB() {
//   if (digitalRead(2) == LOW) counter--;
//   else counter++;
// }
