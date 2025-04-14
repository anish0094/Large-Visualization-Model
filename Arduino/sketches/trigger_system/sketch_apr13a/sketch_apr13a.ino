void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // Wait for serial input (from Python)
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    if (command == "REQUEST_TRIGGER") {
      digitalWrite(LED_BUILTIN, HIGH);  // Visual confirmation
      Serial.println("TRIGGER_AI");     // Send single trigger
      delay(100);                       // Small delay
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}