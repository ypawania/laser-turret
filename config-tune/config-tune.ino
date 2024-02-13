#include <Servo.h>
Servo myservo;
int xPin = A3;
int xVal;
#define button 1
int leftConfig = 0;
int rightConfig = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  myservo.attach(3);  
}

void loop() {
  //Find right and left limits if 
  if(leftConfig == 0 || rightConfig == 0){
    config();
  }

}

void config (){
  xVal = analogRead(xPin);
  myservo.write(map(xVal, 0, 1023, 0, 180));
  
  //save joystck right value when button pressed
  if (leftConfig == 0 && digitalRead(button) == HIGH){
    leftConfig = myservo.read();
  }
  else if (rightConfig == 0 && digitalRead(button == HIGH)){
    rightConfig = myservo.read();
  }
}