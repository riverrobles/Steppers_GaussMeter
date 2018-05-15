int stp1, stp2, stp3, dir1, dir2, dir3, ms11, ms12, ms13, ms21, ms22, ms23;
int stps[] = {stp1,stp2,stp3};
int dirs[] = {dir1,dir2,dir3};
int ms1s[] = {ms11,ms12,ms13};
int ms2s[] = {ms21,ms22,ms23};

int curboard;
String input;

bool backStep();
bool forwardStep();
void clearSerial();
void Pulse();
void resetPins();

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < sizeof(stps); i++) {
    pinMode(stps[i],OUTPUT);
    pinMode(dirs[i],OUTPUT);
    pinMode(ms1s[i],OUTPUT);
    pinMode(ms2s[i],OUTPUT);
  }
  resetPins();
}

void loop() {
  while (Serial.available()==0){}

  input = Serial.readString();
  clearSerial();

  if (isDigit(input.charAt(0))){
    curboard = input.toInt();
    while (Serial.available()==0){}
    input = Serial.readString();
    float steps = input.toFloat();
    if (steps < 0.0){
      if (backStep(-steps)){Serial.println("normal");};
    }
    else if (steps > 0.0){
      if (forwardStep(steps)){Serial.println("normal");};
    }
  }
}

bool forwardStep(float stps){
  digitalWrite(dirs[curboard],HIGH);
  for (long x = 0; x < stps; x++){
    Pulse();
  }
  return true;
}

bool backStep(float stps){
  digitalWrite(dirs[curboard],LOW);
  for (long x = 0; x < stps; x++){
    Pulse();
  }
  return true;
}

void Pulse(){
  digitalWrite(stps[curboard],HIGH);
  delay(1);
  digitalWrite(stps[curboard],LOW);
  delay(1);
}

void clearSerial(){
  while (Serial.available()>0){
    Serial.read();
  }
}

void resetPins(){
  for (int i = 0; i < sizeof(stps); i++){
    digitalWrite(ms1s[i],LOW);
    digitalWrite(ms2s[i],LOW);
  }
}

