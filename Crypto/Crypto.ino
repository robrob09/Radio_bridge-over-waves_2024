// Protection of transmitted information

// encryption script
int encrypt_base(int n, int* inverse, int inverse_num = 0, int Lshift = 0) {
	bool is_inv[32];
	for (int i = 0; i < 32; i++) {
		is_inv[i] = 0;
	}
	for (int i = 0; i < inverse_num; i++) {
		is_inv[inverse[i]] = 1;
	}

	int m = n;
	for (int i = 0; i < 32; i++) {
		if (is_inv[i]) {
			m ^= (1 << i);
		}
	}
	return (m << Lshift);
}

// decryption script
int decrypt_base(int n, int* inverse, int inverse_num = 0, int Lshift = 0) {
	bool is_inv[32];
	for (int i = 0; i < 32; i++) {
		is_inv[i] = 0;
	}
	for (int i = 0; i < inverse_num; i++) {
		is_inv[inverse[i]] = 1;
	}

	int m = (n >> Lshift);
	for (int i = 0; i < 32; i++) {
		if (is_inv[i]) {
			m ^= (1 << i);
		}
	}
	return m;
}
void setup() {
	Serial.begin(9600);
	// sample settings
	int n = 11;
	int m = 36;
	int inverse_num = 1;
	int inverse[inverse_num] = { 1 };
	int Lshift = 2;
	Serial.print("Encrypted ");
	Serial.print(n);
	Serial.print(": ");
	Serial.println(encrypt_base(n, inverse, inverse_num, Lshift));
	Serial.print("Decrypted ");
	Serial.print(m);
	Serial.print(": ");
	Serial.println(decrypt_base(m, inverse, inverse_num, Lshift));
}

void loop() {

}
