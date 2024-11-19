const int fsrPin1 = A0;  
const int fsrPin2 = A1;  
const int fsrPin3 = A2;  

const int ledPin1 = 9;   
const int ledPin2 = 8; 
const int ledPin3 = 7;   

const int pressThreshold = 150;  
const int releaseThreshold = 60;  

bool isPressed1 = false;
bool isPressed2 = false;
bool isPressed3 = false;

void setup() {
  Serial.begin(9600);  
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
}

void loop() {
  // FSR1 Logic
  int fsrValue1 = analogRead(fsrPin1);
  if (fsrValue1 > pressThreshold && !isPressed1) {
    int velocity = constrain(round((fsrValue1 - pressThreshold) * (127.0 / (400 - pressThreshold))), 0, 127);

    Serial.print("1,");
    Serial.print(velocity);
    Serial.println(",1");
    digitalWrite(ledPin1, HIGH);
    isPressed1 = true;
  } else if (fsrValue1 < releaseThreshold && isPressed1) {
    Serial.println("2,-1,0");
    digitalWrite(ledPin1, LOW);
    isPressed1 = false;
  }

  // FSR2 Logic
  int fsrValue2 = analogRead(fsrPin2);
  if (fsrValue2 > pressThreshold && !isPressed2) {
    int velocity = constrain(round((fsrValue2 - pressThreshold) * (127.0 / (400 - pressThreshold))), 0, 127);

    Serial.print("3,");
    Serial.print(velocity);
    Serial.println(",1");
    digitalWrite(ledPin2, HIGH);
    isPressed2 = true;
  } else if (fsrValue2 < releaseThreshold && isPressed2) {
    Serial.println("2,-1,0");
    digitalWrite(ledPin2, LOW);
    isPressed2 = false;
  }

  // FSR3 Logic
  int fsrValue3 = analogRead(fsrPin3);
  if (fsrValue3 > pressThreshold && !isPressed3) {
    int velocity = constrain(round((fsrValue3 - pressThreshold) * (127.0 / (400 - pressThreshold))), 0, 127);

    Serial.print("5,");
    Serial.print(velocity);
    Serial.println(",1");
    digitalWrite(ledPin3, HIGH);
    isPressed3 = true;
  } else if (fsrValue3 < releaseThreshold && isPressed3) {
    Serial.println("2,-1,0");
    digitalWrite(ledPin3, LOW);
    isPressed3 = false;
  }

  delay(5);  // Small delay for stability
}
