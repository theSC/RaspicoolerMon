# RaspicoolerMon

This project is being created to monitor coolers remotely in professional kitches using Arduino Minis and a Rasberry Pi.

Features:
-Wireless communication between Arduinos and Raspberry Pi using NRF24L01s (WIP)
-Outside weather
-RSS feed display (Feed title and top three headlines)
-Cooler tempuratures and humidty using DHT22s (WIP)
-Kitchen tempuarte and humidty using DHT22s (WIP)
-.csv logging (WIP)
-MySQL logging (WIP)
-Pushbullet notifications (WIP)
-Live website HUD (WIP)

Setup:
Open raspicoolermon.py in your favorite text editor and change the directory for the coolermon.log and RSS feed


The wiring for the LCD is as follows:
1 : GND
2 : 5V
3 : Contrast (0-5V)*
4 : RS (Register Select)
5 : R/W (Read Write)       - GROUND THIS PIN
6 : Enable or Strobe
7 : Data Bit 0             - NOT USED
8 : Data Bit 1             - NOT USED
9 : Data Bit 2             - NOT USED
10: Data Bit 3             - NOT USED
11: Data Bit 4
12: Data Bit 5
13: Data Bit 6
14: Data Bit 7
15: LCD Backlight +5V**
16: LCD Backlight GND

Reed switch: Pin 17 (Pulled up)
