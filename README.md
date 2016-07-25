# RaspicoolerMon

This project is being created to monitor coolers remotely in professional kitches using Arduino Minis and a Rasberry Pi.

##Features:##
- 16x2 LCD Display on Raspberry Pi diplays: 
  - Outside weather (Using [PyOWM](https://github.com/csparpa/pyowm). You will need an [OWM](http://openweathermap.org/api) API key)
  - RSS feed display (Feed title and top three headlines)
  - Cooler tempuratures and humidty using DHT22s (WIP)
  - Kitchen tempurature and humidty using DHT22s (WIP)
- Camera capture upon door open using Raspberry Pi camera module
- Wireless communication between Arduinos and Raspberry Pi using NRF24L01s (WIP)
- .csv logging (WIP)
- MySQL logging (WIP)
- Pushbullet notifications (You will need a [Pushbullet API key](https://www.pushbullet.com/)(WIP)
- Live website HUD (WIP)

##Requirements:##
- curl 7.38
- Python 2.7 and packages:
  - [PyOWM](https://github.com/csparpa/pyowm)
  - [feedparser](https://github.com/kurtmckee/feedparser)

##Setup:##
- Create directory for camera captures. Make sure it is writable by the user that will run RaspicoolerMon.
- Create directory for log.  Make sure it is writable by the user that will run RaspicoolerMon.
- Open **raspicoolermon.py** in your favorite text editor and change:
  - directory for the coolermon.log 
  - RSS feed
  - OWM API
  - OWM location
- Open **pushbullet** in your favorite text editor and copy your pushbullet API into API="YOUR API HERE"

##Raspberry Pi Wiring:##
###LCD###
```
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
```
###Reed switch###
```
Reed switch: Pin 17 (Pulled up)
```
###NRF24L01 wiring###

##Arduino wiring:##
###DHT@@ wiring###
###Piezo wiring###
###LED wiring###
###NRF24L01 wiring###

