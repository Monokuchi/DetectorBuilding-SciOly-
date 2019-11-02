  //Variables
  int resistorT=0;  //Thermistor resistance (we are trying to find this)
  int voltageT=0;  //Voltage drop through resistorT
  int resistorK=0;  //Known resistance
  int voltageK=0;  //Voltage drop through resistorK
  int voltageS=9;  //Source voltage


void setup() {
  Serial.begin(9600);
  
}


int voltageDivider(int Rk,int Vs,int Vk)  //returns the value for a unknown resistor value(our resistorT) using a voltage divider
{
  return (((Rk*Vs)/Vk)-Rk);
}


void loop() {
  resistorT=voltageDivider(resistorK,voltageS,voltageK);
  Serial.println(resistorT);
  delay(1000);
}

