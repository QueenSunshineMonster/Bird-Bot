/*
  Discord WebHook Example for Mkr Wifi 1010
*/

#include "discord.h"

void setup() {
  Serial.begin(9600);
  connect_to_wifi();
  discord_send("Hello World");
}

void loop() {
}
