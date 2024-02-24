#include <ESP32Servo.h>
Servo myservo;  
int pos = 0;   

void setup() {
	myservo.setPeriodHertz(50);    
	myservo.attach(18, 500, 2400); 
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){
    pos = Serial.parseInt();
  }  
  
  myservo.write(pos);
  delay(200);
}
