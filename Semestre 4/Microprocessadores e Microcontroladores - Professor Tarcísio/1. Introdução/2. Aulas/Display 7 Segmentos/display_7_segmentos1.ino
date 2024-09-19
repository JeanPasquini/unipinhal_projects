// C++ code
//
void setup()
{
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(4, INPUT);
  pinMode(3, INPUT);
  pinMode(2, INPUT);
}

void loop()
{
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
  digitalWrite(13, LOW);

  if (digitalRead(4) == HIGH && (digitalRead(3) == HIGH && digitalRead(2) == HIGH)) {
    digitalWrite(7, HIGH);
    digitalWrite(8, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(10, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(12, HIGH);
  }
  if (digitalRead(4) == HIGH && (digitalRead(3) == HIGH && digitalRead(2) == HIGH)) {
    digitalWrite(8, HIGH);
    digitalWrite(9, HIGH);
  }
  if (digitalRead(4) == HIGH && (digitalRead(3) == HIGH && digitalRead(2) == HIGH)) {
    digitalWrite(7, HIGH);
    digitalWrite(8, HIGH);
    digitalWrite(13, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(10, HIGH);
  }
  if (digitalRead(4) == LOW && (digitalRead(3) == HIGH && digitalRead(2) == HIGH)) {
    digitalWrite(7, HIGH);
    digitalWrite(8, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(10, HIGH);
    digitalWrite(13, HIGH);
  }
  if (digitalRead(4) == HIGH && (digitalRead(3) == LOW && digitalRead(2) == LOW)) {
    digitalWrite(8, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(13, HIGH);
  }
  if (digitalRead(4) == HIGH && (digitalRead(3) == LOW && digitalRead(2) == HIGH)) {
    digitalWrite(7, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(13, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(10, HIGH);
  }
  if (digitalRead(4) == HIGH && (digitalRead(3) == HIGH && digitalRead(2) == LOW)) {
    digitalWrite(7, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(13, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(10, HIGH);
    digitalWrite(11, HIGH);
  }
  if (digitalRead(4) == HIGH && (digitalRead(3) == HIGH && digitalRead(2) == HIGH)) {
    digitalWrite(7, HIGH);
    digitalWrite(8, HIGH);
    digitalWrite(9, HIGH);
  }
  delay(10); // Delay a little bit to improve simulation performance
}