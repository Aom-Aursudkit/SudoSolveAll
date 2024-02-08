void go(int x) {
  if (x > 100) x = 100;
  if (x < -100) x = -100;
  if (x >= 1) {
    digitalWrite(m1a, HIGH);
    digitalWrite(m1b, LOW);
  }
  if (x <= -1) {
    digitalWrite(m1a, LOW);
    digitalWrite(m1b, HIGH);
    x = x * -1;
  }
  if (x == 0) {
    digitalWrite(m1a, LOW);
    digitalWrite(m1b, LOW);
  }
  int xx = map(x, 0, 100, 0, 255);
  // Serial.println(xx);
  analogWrite(m1en, xx);
}

void readd(int q) {
  error = counter - q;
  Serial.print("   counter:");
  Serial.print(counter);
  Serial.print("   error:");
  Serial.print(error);
}

void pidd() {
  if (PID > 0 && error < 0) I = 0;
  if (PID < 0 && error > 0) I = 0;
  if (P == 0) I = 0;

  P = error;
  I = I + error;
  D = error - errorr;

  PID = (Kp * P) + (Ki * I) + (Kd * D);
  if (PID < -100) PID = -100;
  if (PID > 100) PID = 100;
  Serial.print("   P:");
  Serial.print(P);
  Serial.print("   I:");
  Serial.print(I);
  Serial.print("   D:");
  Serial.print(D);
  Serial.print("   PID:");
  Serial.println(PID);

  errorr = error;
}