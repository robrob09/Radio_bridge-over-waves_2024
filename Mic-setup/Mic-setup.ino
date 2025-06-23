// Microphone setup

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// CE, CSN pins
RF24 radio(9, 10);

// true - transmitter
// false - receiver
bool isTransmitter = true;

void setup() {
	Serial.begin(9600);
	radio.begin();

	radio.setPALevel(RF24_PA_MAX);
	radio.setDataRate(RF24_1MBPS);
	radio.setChannel(112);
	radio.setRetries(15, 15);
	radio.setCRCLength(RF24_CRC_16);

	// The difference for the transmitter and receiver
	if (isTransmitter) {
		radio.openWritingPipe(0xF0F0F0F0E1LL);
		radio.stopListening();
	}
	else {
		radio.openReadingPipe(1, 0xF0F0F0F0E1LL);
		radio.startListening();
	}

	printRadioSettings();
}

char text[] = "Hello";
void loop() {
	// The difference for the transmitter and receiver
	if (isTransmitter) {
		// char text[] = "Hello";
		++text[0];
		radio.write(&text, sizeof(text));
		Serial.println(text);
		delay(1000);
	}
	else {
		if (radio.available()) {
			char text[32] = "";
			radio.read(&text, sizeof(text));
			Serial.println(text);
		}
	}
}

void printRadioSettings() {
	Serial.println(F("RF24 radio settings:"));
	Serial.print(F("RF Channel: "));
	Serial.println(radio.getChannel());

	Serial.print(F("PA Level: "));
	Serial.println(radio.getPALevel());

	Serial.print(F("Data Rate: "));
	Serial.println(radio.getDataRate());

	Serial.print(F("CRC Length: "));
	Serial.println(radio.getCRCLength());

	// Since we can't get the values used in setRetries dynamically, 
	// we'll display the last set values.

	Serial.println(F("Retransmit Delay: 15 * 250μs"));
	Serial.println(F("Retransmit Count: 15"));
}
