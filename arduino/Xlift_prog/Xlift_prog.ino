// #include <CytronMotorDriver.h>
#include <LiquidCrystal.h>

const int sw = 0;
const int pin_RS = 8;
const int pin_EN = 9;
const int pin_d4 = 4;
const int pin_d5 = 5;
const int pin_d6 = 6;
const int pin_d7 = 7;
const int pin_BL = 10;
LiquidCrystal lcd(pin_RS, pin_EN, pin_d4, pin_d5, pin_d6, pin_d7);

int x;
int height = 0;
int limitt = 0;
int limitb = 0;
int stopp = 0;

// CytronMD motor1(PWM_PWM, 12, 13);

const int trig = 31;
int echo = 30;
long duration, cm;
long microsecondsToCentimeters(long microseconds) {
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}

void setup() {
  Serial.begin(9600);
  ////////////////////////////////////////
  pinMode(28, OUTPUT);
  pinMode(44, OUTPUT);
  pinMode(45, OUTPUT);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  ////////////////////////////////////////
  // digitalWrite(22, HIGH);
  // digitalWrite(23, HIGH);
  lcd.begin(16, 2);
  lcd.setCursor(1, 0);
  lcd.print("Press -SELECT-");
  lcd.setCursor(4, 1);
  lcd.print("to start");
  while (!(analogRead(sw) > 700 && analogRead(sw) < 750))
    ;
  lcd.clear();
  lcd.setCursor(1, 0);
  lcd.print("Height:");

  lcd.setCursor(8, 0);
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(5);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  cm = microsecondsToCentimeters(duration) + 20;
  height = cm;
}
void loop() {
  x = analogRead(0);
  lcd.setCursor(8, 0);

  if (digitalRead(28) == HIGH) {
    height = cm;
    stopp = 1;
  }
  if (x < 60) {
    stopp = 0;
    height = 75;
    lcd.setCursor(1, 1);
    lcd.print("-->");
    lcd.setCursor(4, 1);
    lcd.print(height);
    // while (1) {
    //   lcd.setCursor(8, 0);
    //   analogWrite(44, 255);
    //   digitalWrite(45, HIGH);
    //   digitalWrite(trig, LOW);
    //   delayMicroseconds(2);
    //   digitalWrite(trig, HIGH);
    //   delayMicroseconds(5);
    //   digitalWrite(trig, LOW);
    //   duration = pulseIn(echo, HIGH);
    //   cm = microsecondsToCentimeters(duration) + 20;
    //   lcd.print(cm);
    //   delay(2);
    //   lcd.print("        ");
    //   height = cm;
    //   if (cm > 74) break;
    // }
    // analogWrite(44, 0);
    Serial.println("Right");
  }
  /////////////////////////////////
  else if (x < 200) {
    ///////////////////////////////
    height++;
    stopp = 0;
    if (height > 75) height = 75;
    lcd.setCursor(1, 1);
    lcd.print("-->");
    lcd.setCursor(4, 1);
    lcd.print(height);
    delay(220);
    // digitalWrite(22, LOW);
    // digitalWrite(23, HIGH);
    ///////////////////////////////
    // if (cm < 75 && limitt == 0) {
    //   analogWrite(44, 255);
    //   digitalWrite(45, HIGH);
    //   limitb = 0;
    // } else {
    //   analogWrite(44, 0);
    //   limitt = 1;
    // }
    Serial.println("Up");
    // delay(100);
  }
  /////////////////////////////////
  else if (x < 400) {
    ///////////////////////////////
    height--;
    stopp = 0;
    if (height < 58) height = 58;
    lcd.setCursor(1, 1);
    lcd.print("-->");
    lcd.setCursor(4, 1);
    lcd.print(height);
    delay(220);
    // digitalWrite(22, HIGH);
    // digitalWrite(23, LOW);
    ///////////////////////////////
    // if (cm > 58 && limitb == 0) {
    //   analogWrite(44, 255);
    //   digitalWrite(45, LOW);
    //   limitt = 0;
    // } else {
    //   analogWrite(44, 0);
    //   limitb = 1;
    // }
    Serial.println("Down");
    // delay(100);
  }
  /////////////////////////////////
  else if (x < 600) {
    stopp = 0;
    height = 58;
    lcd.setCursor(1, 1);
    lcd.print("-->");
    lcd.setCursor(4, 1);
    lcd.print(height);
    // while (1) {
    //   lcd.setCursor(8, 0);
    //   analogWrite(44, 255);
    //   digitalWrite(45, LOW);
    //   digitalWrite(trig, LOW);
    //   delayMicroseconds(2);
    //   digitalWrite(trig, HIGH);
    //   delayMicroseconds(5);
    //   digitalWrite(trig, LOW);
    //   duration = pulseIn(echo, HIGH);
    //   cm = microsecondsToCentimeters(duration) + 20;
    //   lcd.print(cm);
    //   delay(2);
    //   lcd.print("        ");
    //   height = cm;
    //   if (cm < 59) break;
    // }
    // analogWrite(44, 0);
    Serial.println("Left");
  }
  /////////////////////////////////
  else if (x < 800) {
    Serial.println("Select");
  }
  /////////////////////////////////
  if (height > cm && stopp == 0) {
    if (cm < 75 && limitt == 0) {
      analogWrite(44, 255);
      digitalWrite(45, HIGH);
      limitb = 0;
    } else {
      analogWrite(44, 0);
      limitt = 1;
    }
  }
  /////////////////////////////////
  else if (height < cm && stopp == 0) {

    if (cm > 58 && limitb == 0) {
      analogWrite(44, 255);
      digitalWrite(45, LOW);
      limitt = 0;
    } else {
      analogWrite(44, 0);
      limitb = 1;
    }
  }
  /////////////////////////////////
  else {
    stopp = 1;
    analogWrite(44, 0);
  }
  lcd.setCursor(8, 0);
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(5);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  cm = microsecondsToCentimeters(duration) + 20;
  if (stopp == 1) lcd.print(height);
  else lcd.print(cm);
  delay(2);
  lcd.print("        ");
}