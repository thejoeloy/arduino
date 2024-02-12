int speakerPin = 14;  // A0 as digital pin
int toneFrequency = 440; // Frequency of the tone in Hz

void setup() {
  pinMode(speakerPin, OUTPUT);  // initialize the digital pin as an output.
}

void loop() {
  // Generate a simple square wave
  digitalWrite(speakerPin, HIGH);  // turn the speaker ON
  delayMicroseconds(1000000 / (2 * toneFrequency)); // half of the period (in microseconds) for a 440 Hz wave
  digitalWrite(speakerPin, LOW);  // turn the speaker OFF
  delayMicroseconds(1000000 / (2 * toneFrequency)); // the other half of the period
}
