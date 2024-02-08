#include <Servo.h>

//receiver
#define ch1 13
#define ch2 12
#define ch3 11
#define ch4 10
#define ch5 9

//motor driver
#define m1a 8
#define m1b 7
#define m1en 6
#define m2a 4
#define m2b 2
#define m2en 5

//servo
#define serv 3
Servo servo;

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

int m1;
int m2;

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
  pinMode(m1b, OUTPUT);
  pinMode(m1en, OUTPUT);
  ///////////////////////
  pinMode(m2a, OUTPUT);
  pinMode(m2b, OUTPUT);
  pinMode(m2en, OUTPUT);
  ///////////////////////
  servo.attach(serv);
  servo.write(0); 
  // attachInterrupt(digitalPinToInterrupt(RCch3), PulseTimer, CHANGE);
}

void loop() {
  /////////////////////////////////////
  m1 = RCchV(ch2, -100, 100) + RCchV(ch1, -100, 100);
  m2 = RCchV(ch2, -100, 100) - RCchV(ch1, -100, 100);
  go(m1, m2);
  /////////////////////////////////////
  servo.write(RCchV(ch3, 0, 150));
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
