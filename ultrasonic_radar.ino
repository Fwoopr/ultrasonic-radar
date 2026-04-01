#include <Servo.h>
// -- Pin Definitions --
int servoPin = 9;
int echoPin = 12;
int trigPin = 11;
// -- Movement and Timing Setup --
Servo myServo;
int servoPos = 90;
int sweepDir = 1;
unsigned long currentTime;
unsigned long lastMove = 0;
unsigned long delayTime = 100;


void setup() {

  myServo.attach(servoPin);
  pinMode(echoPin,INPUT);
  pinMode(trigPin,OUTPUT);
  Serial.begin(115200);
  // Starting Position
  myServo.write(servoPos);

}


void loop() {
  
  currentTime = millis();

  // Start the process every 100 miliseconds
  if (currentTime - lastMove >= delayTime) {
    lastMove = currentTime;

    myServo.write(servoPos);

    float distance = get_distance();

    // Print the measurement values to the Serial Monitor
    Serial.print(servoPos);
    Serial.print(",");
    Serial.println(distance);

    // Change the direction at the limit angle
    servoPos += sweepDir * 5;
    if (servoPos >= 160 || servoPos <= 20) {
      sweepDir = sweepDir * -1;
    }
  }

  

}
// Distance Measurement
float get_distance() {
  
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);

  long ping = pulseIn(echoPin,HIGH);

  float distance = (ping/2.)*0.03432;
  // if out of range, set the distance to 400 cm
  return (distance==0) ? 400 : distance;

}
