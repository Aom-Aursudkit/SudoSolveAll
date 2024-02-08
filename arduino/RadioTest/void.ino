void go(int x, int y) {
  if (x > 100) x = 100;
  if (x < -100) x = -100;
  if (y > 100) y = 100;
  if (y < -100) y = -100;
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
  if (y >= 1) {
    digitalWrite(m2a, HIGH);
    digitalWrite(m2b, LOW);
  } 
  if (y <= -1) {
    digitalWrite(m2a, LOW);
    digitalWrite(m2b, HIGH);
    y = y * -1;
  } 
  if (y == 0) {
    digitalWrite(m2a, LOW);
    digitalWrite(m2b, LOW);
  }
  int xx = map(x, 0, 100, 0, 255);
  int yy = map(y, 0, 100, 0, 255);
  Serial.print(xx);
  Serial.println(yy);
  analogWrite(m1en, xx);
  analogWrite(m2en, yy);
}