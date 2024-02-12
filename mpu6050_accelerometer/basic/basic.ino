#include "I2Cdev.h"
#include "MPU6050.h"

MPU6050 mpu;

void setup() {
  // Initialize Serial communication
  Serial.begin(115200);
  
  // Initialize the 'Wire' class for the I2C bus
  Wire.begin();

  // Initialize MPU6050
  Serial.println("Initialize MPU6050");
  mpu.initialize();
  Serial.println(mpu.testConnection() ? "Connected" : "Connection failed");
}

void loop() {
  // Get current values from MPU6050
  int16_t ax, ay, az, gx, gy, gz;
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

  // Print out values to console
  Serial.print("Ax: "); Serial.print(ax);
  Serial.print(" Ay: "); Serial.print(ay);
  Serial.print(" Az: "); Serial.print(az);
  Serial.print(" Gx: "); Serial.print(gx);
  Serial.print(" Gy: "); Serial.print(gy);
  Serial.print(" Gz: "); Serial.println(gz);

  // Wait before taking new readings
  delay(100);
}
