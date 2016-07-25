#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import netifaces as ni
from datetime import datetime
import pyowm
import re
import logging
import feedparser
import subprocess
from picamera import PiCamera

camera = PiCamera()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18


# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

screen_delay = 5

rssurl = 'YOUR RSS FEED HERE'
owmapi = 'YOUR OWM API KEY HERE'
location = 'YOUR LOCATION HERE ex Vancouver, BC'

logger = logging.getLogger('raspicoolermon')
hdlr = logging.FileHandler('logs/raspicoolermon.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)


def dooropen(channel):
    timenow = time.strftime('%H:%M:%S')
    print "%s Door opened" % timenow
    subprocess.call("./pushbullet 'Door' 'opened @ %s'" % timenow, shell=True)
    time.sleep(3)
    camera.capture('camera_captures/door-open-%s.jpg' % timenow)
    print "Image captured door-open-%s.jpg" % timenow
    logger.info('Door opened')

def main():
  # Main program block
  
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7

  ip = ni.ifaddresses('wlan0')[2][0]['addr']
  
    # Initialise display
  lcd_init()
  lcd_string("Hello!",LCD_LINE_1)
  lcd_string("Setting up...",LCD_LINE_2)
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("~~       RaspicoolerMon        ~~")
  print("~~       --------------        ~~")
  print("~~  Created by: Troy Lundgren  ~~")
  print("~~   troy.lundgren@gmail.com   ~~")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("IP: %s" % ip)
  timenow = time.strftime('%H:%M')
  print("Time is now %s" % timenow)
  print("RSS feed: %s" % rssurl)
  logger.info('Coolermon starting up...')
  logger.info('IP = %s'% ip)
  time.sleep(5) # 3 second delay
  currenttime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  lcd_string("%s" % currenttime,LCD_LINE_1)
  lcd_string("%s" % ip,LCD_LINE_2)
  time.sleep(5)
  print("Entering main loop")
  print("Press: Ctrl+C to exit...")
  GPIO.add_event_detect(17, GPIO.FALLING, callback=dooropen)
  while True:
    try:
      timeshort = time.strftime('%H:%M')
      currenttime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      owm = pyowm.OWM('%s' % owmapi)
      observation = owm.weather_at_place('%s' % location)
      w = observation.get_weather()
      ct = w.get_temperature(unit='celsius')
      ctemp = re.search(r"(?<='temp': ).*?(?=, 'temp_min)", '%s' % ct).group(0)
      sunset = w.get_sunset_time('iso')
      sunrise = w.get_sunrise_time('iso')
      current = w.get_detailed_status() 

      lcd_string("Out temp:  %s" % timeshort,LCD_LINE_1)
      lcd_string("%s celsius" % ctemp,LCD_LINE_2)

      time.sleep(screen_delay)

      lcd_string("Currently: %s" % timeshort,LCD_LINE_1)
      lcd_string("%s" % current,LCD_LINE_2)

      time.sleep(screen_delay)

    except Exception as ex:
      template = "An exception of type {0} occured. Arguments:\n{1!r}"
      message = template.format(type(ex).__name__, ex.args)
      print message 
      lcd_string("ERROR! Unable",LCD_LINE_1)
      lcd_string("to get weather",LCD_LINE_2)
      time.sleep(5)
      logger.exception('Unable to get weather - %s' % message)
      print("ERROR! Unable to get weather")
    finally:
      lcd_string("Date:      Time:",LCD_LINE_1)
      lcd_string("%s" % currenttime,LCD_LINE_2)

      time.sleep(screen_delay)
      try:
        str_pad = " " * 16
        feed = feedparser.parse(rssurl)
        feed_title = feed['feed']['title']
        entry1 = feed['entries'][0]['title']
        entry1_long_string = entry1
        entry1_long_string = str_pad + entry1_long_string
        timeshort = time.strftime('%H:%M')
        lcd_string("%s:%s" % (feed_title, timeshort), LCD_LINE_1)
        for i in range (0, len(entry1_long_string)):
         lcd_byte(LCD_LINE_2, LCD_CMD)
         lcd_text = entry1_long_string[i:(i+15)]
         lcd_string(lcd_text,LCD_LINE_2)
         time.sleep(0.2)

        entry2 = feed['entries'][1]['title']
        entry2_long_string = entry2
        entry2_long_string = str_pad + entry2_long_string
        for i in range (0, len(entry2_long_string)):
         lcd_byte(LCD_LINE_1, LCD_CMD)
         lcd_text = entry2_long_string[i:(i+15)]
         lcd_string(lcd_text,LCD_LINE_2)
         time.sleep(0.2)

        entry3 = feed['entries'][2]['title']
        entry3_long_string = entry3
        entry3_long_string = str_pad + entry3_long_string
        for i in range (0, len(entry3_long_string)):
         lcd_byte(LCD_LINE_1, LCD_CMD)
         lcd_text = entry3_long_string[i:(i+15)]
         lcd_string(lcd_text,LCD_LINE_2)
         time.sleep(0.2)

      except Exception as ex:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message
        lcd_string("ERROR! Unable",LCD_LINE_1)
        lcd_string("to get RSS",LCD_LINE_2)
        time.sleep(5)
        logger.exception('Unable to get RSS feed - %s' % message)
        print("ERROR! Unable to get RSS feed")
      finally:
        time.sleep(1)

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command

  GPIO.output(LCD_RS, mode) # RS

  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display




  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("Goodbye!",LCD_LINE_1)
    logger.info('Keyboard interupt')
    GPIO.cleanup()
