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
- A [RaspberryPi](https://www.amazon.ca/Raspberry-Pi-RASP-PI-3-Model-Board/dp/B01CD5VC92/ref=sr_1_2?ie=UTF8&qid=1469435657&sr=8-2&keywords=raspberry+pi+3)
- [Arduino Nanos](https://www.amazon.ca/gp/product/B00761NDHI/ref=oh_aui_detailpage_o04_s00?ie=UTF8&psc=1)
- A [16x2 LCD](https://www.amazon.ca/CARCHET-Character-Display-Module-Blacklight/dp/B00CJ8RXR4/ref=sr_1_1?ie=UTF8&qid=1469435416&sr=8-1&keywords=16x2+lcd) 
- [Reed switches](https://www.amazon.ca/gp/product/B00OK67B4I/ref=oh_aui_detailpage_o07_s00?ie=UTF8&psc=1)
- [nRF24L01+s](https://www.amazon.ca/gp/product/B01C3YNGI8/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1)
- [Raspberry Pi Camera module](https://www.amazon.ca/gp/product/B00FGKYHXA/ref=oh_aui_detailpage_o04_s00?ie=UTF8&psc=1)
- [DHT22s](https://www.amazon.ca/gp/product/B00XDSOZ2K/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1)
- curl 7.38
- Python 2.7 and packages:
  - [PyOWM](https://github.com/csparpa/pyowm)
  - [feedparser](http://www.pythonforbeginners.com/feedparser/using-feedparser-in-python)

##Setup:##
- Open **raspicoolermon.py** in your favorite text editor and change:
  - RSS feed
  - OWM API
  - OWM location
  - Enable(1)/disable(0) pushbullet notifications
  - Enable(1)/disable(0) camera capture
- Open **pushbullet** in your favorite text editor and copy your pushbullet API into API="YOUR API HERE"
- From insode RaspicoolerMon directory run:  
  - `sudo chmod +x pushbullet`
  - `sudo chmod +x raspicoolermon.py`

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
###DHT22 wiring###
###Piezo wiring###
###LED wiring###
###NRF24L01 wiring###

##Known bugs##

