// Using a potentiometer with a microphone
// Attempt 1

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// The pin number to which the potentiometer is connected
#define PIN_POT A7

// The number pin to which the CE pin of the radio module is connected
#define PIN_CE  10

// The pin number to which the CSN output of the radio module is connected
#define PIN_CSN 9

RF24 radio(PIN_CE, PIN_CSN);

// Array for transmitting potentiometer values
int potValue[1];

void setup() {
	Serial.begin(9600);
	radio.begin();

	radio.setChannel(4);
	radio.setDataRate(RF24_1MBPS);
	radio.setPALevel(RF24_PA_HIGH);
	radio.openWritingPipe(0x7878787878LL);
}

void loop() {
	// potValue[0] = analogRead(PIN_POT);
	Serial.println(radio.available());
	potValue[0] = 2;

	// We send readings over the radio channel
	radio.write(potValue, 1);
}
