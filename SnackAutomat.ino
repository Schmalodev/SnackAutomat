#include <Servo.h> //Hir hollen wir uns den Servo Bibliothek

Servo downFall; // Dort sagen wir das ein Servo motor DownFall heist

void setup() {
  Serial.begin(9600);
  downFall.attach(9); //Wir sagen das pin ~9 verwendet werden soll
  downFall.write(0);
}

void loop() {
  if(Serial.available() > 0){
    String command = Serial.readString();

    if(command == "turn"){
      downFall.write(0);
      delay(1000);
      downFall.write(90);
      delay(1000);
      downFall.write(0);
    }
  }
}
