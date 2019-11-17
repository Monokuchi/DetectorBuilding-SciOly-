 //Variables
  float resistorT=0;  //Thermistor resistance (we are trying to find this)
  float voltageT=0;  //Voltage drop through resistorT
  float resistorK=22000.0;  //Known resistance
  float voltageK=0.0;  //Voltage drop through resistorK
  float voltageS=5.0;  //Source voltage
  float analogVoltagePin=A0;

void setup() {
  Serial.begin(9600);
 
  
}


float voltageDivider(float Rk,float Vs,float Vk)  //returns the value for a unknown resistor value(our resistorT) using a voltage divider
{
  return (((Rk*Vs)/Vk)-Rk);
}


void loop() {
  float voltageDrop=analogRead(analogVoltagePin);
  // voltageK=map(voltageDrop, 0.0, 1023.0, 0.0, 5.0);
  voltageK = voltageDrop*5/1023;  //ghetto map
  resistorT=voltageDivider(resistorK,voltageS,voltageK);
  Serial.print(voltageK);  //Blue
  Serial.print("\t");
  Serial.println(resistorT);  //Red

  delay(100);
}
