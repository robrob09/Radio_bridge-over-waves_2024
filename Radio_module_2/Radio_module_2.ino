// Using a potentiometer with a microphone
// Attempt 2

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// The pin number to which the LED is connected
#define PIN_LED 3

// The pin number to which the CE is connected
#define PIN_CE  10

// The pin number to which the CSN is connected
#define PIN_CSN 9

RF24 radio(PIN_CE, PIN_CSN);

// Array for transmitting potentiometer values
int potValue[1];

void setup() {
	Serial.begin(9600);
	pinMode(PIN_LED, OUTPUT);
	radio.begin();

	radio.setChannel(4);
	radio.setDataRate(RF24_1MBPS);
	radio.setPALevel(RF24_PA_HIGH);
	radio.openReadingPipe(1, 0x7878787878LL);
	radio.startListening();
}

void loop() {
	if (radio.available()) {
		radio.read(&potValue, sizeof(potValue));
		Serial.println(potValue[0]);
		/*
		// Adjust the brightness of the diode
		analogWrite(PIN_LED, map(potValue[0],0,1023,0,255));
		*/
	}
}
