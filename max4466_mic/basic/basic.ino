// Pin where the microphone is connected to
const int microphonePin = A0;

void setup() {
  // Initialize serial communication at 9600 bps
  Serial.begin(9600);
}

void loop() {
  // Read the value from the analog sensor
  int sensorValue = analogRead(microphonePin);
  
  // Print the sensor value to the serial monitor
  Serial.println(sensorValue);

  // Delay to make it readable
  delay(100);
}

