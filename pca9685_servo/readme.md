# Arduino-based Servo Controller

## Parts
- Metro Mini
- PCA 9685
- Micro servo motor

## Metro Mini to PCA 9685 Connections
1. **5V to VCC**: Connect the 5V pin on the Metro Mini to the VCC pin on the PCA 9685.
2. **5V to V+**: Connect the 5V pin on the Metro Mini to the V+ pin on the PCA 9685.
3. **GND to GND**: Connect the GND pin on the Metro Mini to the GND pin on the PCA 9685.
4. **A4 to SDA**: Connect the SDA pin on the Metro Mini to the SDA pin on the PCA 9685.
5. **A5 to SCL**: Connect the SCL pin on the Metro Mini to the SCL pin on the PCA 9685.

## PCA 9685 to Micro Servo Connections
1. **Servo Signal**: Connect the PWM output channel on the PCA 9685 to the signal wire (often orange or yellow) of the micro servo.
2. **Servo Power**: Connect the V+ (sometimes labeled as 'Servo VCC' or just 'V') on the PCA 9685 to the power wire (often red) of the micro servo.
3. **Servo Ground**: Connect the GND pin associated with the PCA 9685's PWM output channel to the ground wire (often brown or black) of the micro servo.




