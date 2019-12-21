 //Variables & Libaries
  #include <ExtendedADCShield.h>
  #include <SPI.h>
  ExtendedADCShield extendedADCShield(16);

  float resistorT=0;  //Thermistor resistance (we are trying to find this)
  float voltageT=0;  //Voltage drop through resistorT
  float resistorK=22000.0;  //Known resistance
  float voltageK=0.0;  //Voltage drop through resistorK
  float voltageS=5.0;  //Source voltage
  float analogVoltagePin=A0;
  float ch0;
  
void setup() {
  Serial.begin(9600);
  SPI.begin();
  extendedADCShield.analogReadConfigNext(0, SINGLE_ENDED, UNIPOLAR, RANGE5V);
}


float voltageDivider(float Rk,float Vs,float Vk)  //returns the value for a unknown resistor value(our resistorT) using a voltage divider
{
  return (((Rk*Vs)/Vk)-Rk);
}


void loop() {
  ch0 =  extendedADCShield.analogReadConfigNext(0, SINGLE_ENDED, UNIPOLAR, RANGE5V);
  Serial.println(ch0,4);
  delay (1000);


  
  voltageK = ch0;
  resistorT=voltageDivider(resistorK,voltageS,voltageK);
//  Serial.print(voltageK);  //Blue
//  Serial.print("\t");
//  Serial.println(resistorT);  //Red
//  delay(100);
}
