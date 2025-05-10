#include <Servo.h> //Hir hollen wir uns den Servo Bibliothek

Servo downFall; // Dort sagen wir das ein Servo motor DownFall heist

void setup() {
  downFall.attach(9); //Wir sagen das pin ~9 verwendet werden soll
}

void loop() {
  downFall.write(0); //DownFall soll sich auf pos 0 drehen
  delay(1000); //Verzögerung von 1 sek
  downFall.write(90);
  delay(1000);
}
