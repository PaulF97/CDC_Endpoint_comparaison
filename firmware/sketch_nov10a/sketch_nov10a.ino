String incomingByte ;    

char serialArrayTest[64];

void setup() {

  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);

  for(int i = 0; i<sizeof(serialArrayTest); i++){
    serialArrayTest[i] = 'Paul';
  }
  
}

void loop() {


  if (Serial.available() > 0) {

  incomingByte = Serial.readStringUntil('\n');

    if (incomingByte == "paul") {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.write((char*)serialArrayTest, sizeof(serialArrayTest));
    }
  }
}
