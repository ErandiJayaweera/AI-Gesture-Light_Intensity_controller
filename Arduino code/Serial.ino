
int  l;
int pwm_val;

void setup() {
Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0)
  {
    l = Serial.read();
    pwm_val = map(l,97,122,0,255);
    analogWrite(3,pwm_val);
  }
}
