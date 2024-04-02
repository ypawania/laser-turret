#include <ESP32Servo.h>
Servo Xservo;  
Servo Yservo;
int pos = 0;   
boolean startbit = false;
boolean newlinerecieved = false;
String inputString = "";
String recieved_data = "";
int incomingByte = 0;
void on_recieve();
String motor;
int angle;

int leftCon = 65;
int rightCon = 125;
int upCon = 40;
int downCon = 13;

void setup() {
	Xservo.setPeriodHertz(50);   
  Yservo.setPeriodHertz(50); 
	Xservo.attach(18, 500, 2400); 
  Yservo.attach(19, 500, 2900);
  Serial.begin(9600);
}


void loop() {
  if (Serial.available() > 0){
    incomingByte = Serial.read();
    if (incomingByte == '%'){
      startbit = true;
    }
    if (startbit == true){
      inputString += (char) incomingByte;
    }
    if (startbit == true && incomingByte == '#'){
      newlinerecieved = true;
      startbit = false;
    }
    if (newlinerecieved == true){
      recieved_data = inputString.substring(1, (inputString.length() - 1));
      inputString = "";
      newlinerecieved = false;
      on_recieve();
    }

  }  
}
void on_recieve(){
    motor = recieved_data.substring(0,1);
    int coordinate = recieved_data.substring(1, recieved_data.length()).toInt();

    if (motor == "X"){
      angle = map(coordinate, 620, 10, leftCon, rightCon);
      Xservo.write(angle);
      delay(30);
    }
    else if (motor == "Y"){
      angle = map(coordinate, 450, 10, downCon, upCon);
      Yservo.write(angle);
      delay(30);
    }
    
  }

