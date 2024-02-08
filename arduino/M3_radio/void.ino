// void go(float a, float b, float c, float d) {
//   if (a > 100) a = 100;
//   if (a < -100) a = -100;
//   if (b > 100) b = 100;
//   if (b < -100) b = -100;
//   if (c > 100) c = 100;
//   if (c < -100) c = -100;
//   if (d > 100) d = 100;
//   if (d < -100) d = -100;
//   if (a >= 1) {
//     digitalWrite(m1, HIGH);
//   } 
//   if (a <= -1) {
//     digitalWrite(m1, LOW);
//     a = a * -1;
//   } 
//   if (b >= 1) {
//     digitalWrite(m2, HIGH);
//   } 
//   if (b <= -1) {
//     digitalWrite(m2, LOW);
//     b = b * -1;
//   } 
//   if (c >= 1) {
//     digitalWrite(m3, HIGH);
//   } 
//   if (c <= -1) {
//     digitalWrite(m3, LOW);
//     c = c * -1;
//   } 
//   if (d >= 1) {
//     digitalWrite(m4, HIGH);
//   } 
//   if (d <= -1) {
//     digitalWrite(m4, LOW);
//     d = d * -1;
//   } 
//   float aa = map(a, 0, 100, 0, 255);
//   float bb = map(b, 0, 100, 0, 255);
//   float cc = map(a, 0, 100, 0, 255);
//   float dd = map(b, 0, 100, 0, 255);
//   Serial.print(aa);
//   Serial.print(bb);
//   Serial.print(cc);
//   Serial.println(dd);
//   analogWrite(m1en, aa);
//   analogWrite(m2en, bb);
//   analogWrite(m3en, cc);
//   analogWrite(m4en, dd);
// }

void go(float x, float y) {
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
  float xx = map(x, 0, 100, 0, 255);
  float yy = map(y, 0, 100, 0, 255);
  Serial.print(xx);
  Serial.println(yy);
  analogWrite(m1en, xx);
  analogWrite(m2en, yy);
}