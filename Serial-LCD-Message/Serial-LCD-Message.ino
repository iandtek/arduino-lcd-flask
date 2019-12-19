// include the library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("hello, world!");
  Serial.begin(9600);           // set up Serial library at 9600 bps
}


// the loop function runs over and over again forever
void loop() {
  while (Serial.available()) {
    delay(3);  //delay to allow buffer to fill
    if (Serial.available() >0) {
      String message = Serial.readString();
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print(message);
    }
  }
}
