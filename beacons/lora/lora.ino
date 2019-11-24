#include <SPI.h>
#include <RH_RF95.h>

#define RFM95_CS 8
#define RFM95_RST 4
#define RFM95_INT 3

#define RF95_FREQ 927.0

char *flag = "This is VE3IRR. Signal identification challenge #14: flag{ch1rP_spr3Ad_sp3c7ruM_i5_fuN}";
RH_RF95 rf95(RFM95_CS, RFM95_INT);

void setup() 
{
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);

  delay(100);

  // manual reset
  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);

  while (!rf95.init()) {
    // LoRa radio init failed
    while (1);
  }

  if (!rf95.setFrequency(RF95_FREQ)) {
    // setFrequency failed
    while (1);
  }
  
  // The default transmitter power is 13dBm, using PA_BOOST.
  // If you are using RFM95/96/97/98 modules which uses the PA_BOOST transmitter pin, then 
  // you can set transmitter powers from 5 to 23 dBm:
  rf95.setTxPower(18, false);
}

void loop()
{
  delay(10);
  rf95.setSignalBandwidth(125000);
  rf95.setSpreadingFactor(10);
  rf95.setCodingRate4(8);
  rf95.setPayloadCRC(true);
  rf95.send((uint8_t *)flag, strlen(flag));

  delay(10);
  rf95.waitPacketSent();

  delay(2000);
}
