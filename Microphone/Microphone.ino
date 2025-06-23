// Attempt to get data from the microphone

const int Window = 23;
// 0 - Out, 1 - Gain, 2 - AR
int pin[3] = { 14, 15, 16 };
unsigned int sample[3];

void setup() {
    Serial.begin(9600);
}

void loop() {
    unsigned long startMillis = millis();
    unsigned int peakToPeak = 0;

    unsigned int signalMax = 0;
    unsigned int signalMin = 1024;

    while (millis() - startMillis < Window) {
        unsigned int Out = analogRead(0);
        if (Out < 1024) {
            if (Out > signalMax) {
                signalMax = Out;
            }
            else if (Out < signalMin) {
                signalMin = Out;
            }
        }
    }
    peakToPeak = signalMax - signalMin;
    double volts = (peakToPeak * 5.0) / 1024;
    Serial.println(volts);
}
