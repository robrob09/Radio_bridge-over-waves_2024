// Fast reading from Arduino

void setup() {
	Serial.begin(115200);
	// Setting the ADC pre-divider to 16 (faster sampling rate)
	ADCSRA |= (1 << ADPS2);
	ADCSRA &= ~(1 << ADPS1) & ~(1 << ADPS0);
}

void loop() {
	// Reading from the analog pin A0
	int sensorValue = analogRead(A0);

	// Sending the value to the computer
	Serial.println(sensorValue);

	// Delay to control the sampling rate
	delayMicroseconds(100);
}
