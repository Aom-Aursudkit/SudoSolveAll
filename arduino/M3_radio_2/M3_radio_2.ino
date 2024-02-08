#include <Servo.h>

//receiver
#define ch1 14 //analog 0
#define ch2 15 //analog 1
#define ch3 16 //analog 2
#define ch4 17 //analog 3
#define ch5 18 //analog 4

//motor driver
#define m1a 12 //3
#define m1en 10
#define m2a 11 //2
#define m2en 13

//servo
#define serv1 3 //arm
#define serv2 5 //tower
#define serv3 6 //grip
Servo servo1; //arm
Servo servo2; //tower
Servo servo3; //grip

int RCchV(int chan, int maplow, int maphigh) {
  int RCchVV = pulseIn(chan, HIGH);
  if (RCchVV >= 1990) {
    RCchVV = 1999;
  }
  if (RCchVV <= 992) {
    RCchVV = 983;
  }
  // Serial.print(RCchVV);
  RCchVV = map(RCchVV, 983, 1999, maplow, maphigh);
  if (chan != 3 && RCchVV < 5 && RCchVV > -5) {
    RCchVV = 0;
  }
  return (RCchVV);
}

int m1 = 0;
int m2 = 0;

int box = 0;
int grip = 0;

// volatile long StartTime = 0;
// volatile long CurrentTime = 0;
// volatile long Pulses = 0;
// int PulseWidth = 0;

void setup() {
  Serial.begin(9600);
  ///////////////////////
  pinMode(ch1, INPUT);
  pinMode(ch2, INPUT);
  pinMode(ch3, INPUT);
  pinMode(ch4, INPUT);
  pinMode(ch5, INPUT);
  ///////////////////////
  pinMode(m1a, OUTPUT);
  pinMode(m1en, OUTPUT);
  ///////////////////////
  pinMode(m2a, OUTPUT);
  pinMode(m2en, OUTPUT);
  ///////////////////////
  servo1.attach(serv1);
  servo2.attach(serv2);
  servo3.attach(serv3);
   
  servo1.write(0);
  servo2.write(90);
  servo3.write(0);
  // attachInterrupt(digitalPinToInterrupt(RCch3), PulseTimer, CHANGE);
}

void loop() {
  /////////////////////////////////////
  m1 = RCchV(ch2, -100, 100) + RCchV(ch1, -100, 100);
  m2 = RCchV(ch2, -100, 100) - RCchV(ch1, -100, 100);
  go(m1, m2);
  /////////////////////////////////////
  if (RCchV(ch3, -100, 100) > 90) servo1.write(0);
  if (RCchV(ch3, -100, 100) < -90) servo1.write(105);
  if (RCchV(ch4, -100, 100) > 50) grip = 1;
  if (RCchV(ch4, -100, 100) < -50) grip = 0;
  if (grip == 0) servo3.write(0);
  if (grip == 1) servo3.write(45);
  if (RCchV(ch5, -100, 100) <= 0) {
    box = 0;
    servo2.write(90);
  }
  if (RCchV(ch5, -100, 100) > 0 && box == 0) {
    box = 1;
    servo2.write(150);
    delay(400);
    servo2.write(40);
    delay(150);
    servo2.write(90);
  }
  /////////////////////////////////////
  // RCch3V = pulseIn(RCch3, HIGH);
  // if (RCch3V >= 1990) {
  //   RCch3V = 1999;
  // }
  // if (RCch3V <= 990) {
  //   RCch3V = 983;
  // }
  // // Serial.print(RCch3V);
  // RCch3VV = map(RCch3V, 983, 1999, -100, 100);
  // if (RCch3VV < 2 && RCch3VV > -2) {
  //   RCch3VV = 0;
  // }
  // Serial.println(RCch3VV);
  // if (Pulses < 2000){
  //   PulseWidth = Pulses;
  // }
  // if (Pulses <= 992){
  //   PulseWidth = 988;
  // }
  // Serial.println(PulseWidth);
}

// void PulseTimer() {
//   CurrentTime = micros();
//   if (CurrentTime > StartTime) {
//     Pulses = CurrentTime - StartTime;
//     StartTime = CurrentTime;
//   }
// }
