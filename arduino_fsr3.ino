const int fsrPin1 = A0;  
const int fsrPin2 = A3;  
const int fsrPin3 = A5;  


const int ledPin1 = 9;   
const int ledPin2 = 8; 
const int ledPin3 = 7;   

const int pressThreshold = 150;  
const int releaseThreshold = 60;  
const float alpha = 0.7;  

float smoothedValue1 = 0;  // Corrected variable names for smoothing
float smoothedValue2 = 0;  

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
  // int rawValue1 = analogRead(fsrPin1);  // Read raw FSR values
  // int rawValue2 = analogRead(fsrPin2);

  int smoothedValue1 = analogRead(fsrPin1);  // Read raw FSR values
  int smoothedValue2 = analogRead(fsrPin2);
  int smoothedValue3 = analogRead(fsrPin3);


  // // Apply low-pass filter smoothing
  // smoothedValue1 = alpha * rawValue1 + (1 - alpha) * smoothedValue1;
  // smoothedValue2 = alpha * rawValue2 + (1 - alpha) * smoothedValue2;

  // FSR1 Logic
  if (smoothedValue1 > pressThreshold && !isPressed1) {
    int velocity = constrain(round((smoothedValue1 - pressThreshold) * (127.0 / (400 - pressThreshold))), 0, 127);

    Serial.print("11,");
    Serial.print(velocity);
    Serial.println(",1");
    digitalWrite(ledPin1, HIGH);
    isPressed1 = true;
  } else if (smoothedValue1 < releaseThreshold && isPressed1) {
    Serial.println("11,-1,0");
    digitalWrite(ledPin1, LOW);
    isPressed1 = false;
  }

  // FSR2 Logic
  if (smoothedValue2 > pressThreshold && !isPressed2) {
    int velocity = constrain(round((smoothedValue2 - pressThreshold) * (127.0 / (400 - pressThreshold))), 0, 127);
    Serial.print("12,");
    Serial.print(velocity);
    Serial.println(",1");
    digitalWrite(ledPin2, HIGH);
    isPressed2 = true;
  } else if (smoothedValue2 < releaseThreshold && isPressed2) {
    Serial.println("12,-1,0");
    digitalWrite(ledPin2, LOW);
    isPressed2 = false;
  }

    // FSR1 Logic
  if (smoothedValue3 > pressThreshold && !isPressed3) {
    int velocity = constrain(round((smoothedValue3 - pressThreshold) * (127.0 / (400 - pressThreshold))), 0, 127);

    Serial.print("11,");
    Serial.print(velocity);
    Serial.println(",1");
    digitalWrite(ledPin3, HIGH);
    isPressed3 = true;
  } else if (smoothedValue3 < releaseThreshold && isPressed3) {
    Serial.println("13,-1,0");
    digitalWrite(ledPin3, LOW);
    isPressed3 = false;
  }

  delay(5);
}
