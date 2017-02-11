/*
   ボタンを押すと 1 を通知
*/
const int pinNum = 8;
boolean btnState = 1;
boolean btnStatePast = 0;

void setup() {
  pinMode(pinNum, INPUT);
  Serial.begin(9600);
}

void loop() {
  btnState = digitalRead(pinNum);
  if (btnState != btnStatePast) {
    if (btnState) {
      Serial.print(1);
    }
    btnStatePast = btnState;
    delay(10); // チャタリング防止
  }
}
