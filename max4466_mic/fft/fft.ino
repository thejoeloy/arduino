const int microphonePin = A0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int value = analogRead(microphonePin);
  Serial.println(value);
  delay(0); // Smallest delay, essentially non-blocking
}

