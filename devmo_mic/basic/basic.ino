// Declare variables
const int micPin = A0;  // Microphone sensor connected to Analog pin A0
int micValue = 0;       // Variable to store the microphone output

void setup() {
  Serial.begin(9600); // Initialize Serial communication at 9600 baud rate
}

void loop() {
  // Read the analog value from the microphone sensor
  micValue = analogRead(micPin);
  
  // Output the sensor value to the console (Serial Monitor)
  Serial.println("Microphone sensor value: ");
  Serial.println(micValue);

  // Small delay for stability
  delay(100);
}

