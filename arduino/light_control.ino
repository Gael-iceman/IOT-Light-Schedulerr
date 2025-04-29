#include <RTClib.h>  // Install Adafruit RTClib if you want real time

RTC_DS3231 rtc;      // If you have a real time clock module (DS3231)
String onTime = "00:00";
String offTime = "00:00";
bool lightOn = false;
int relayPin = 7;

void setup() {
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW);

  if (!rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1);
  }
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    int commaIndex = input.indexOf(',');
    if (commaIndex != -1) {
      onTime = input.substring(0, commaIndex);
      offTime = input.substring(commaIndex + 1);
      Serial.println("Updated schedule");
    }
  }

  DateTime now = rtc.now();
  String currentTime = String(now.hour()) + ":" + (now.minute() < 10 ? "0" : "") + String(now.minute());

  if (currentTime == onTime) {
    digitalWrite(relayPin, HIGH);
    lightOn = true;
  } else if (currentTime == offTime) {
    digitalWrite(relayPin, LOW);
    lightOn = false;
  }
}
