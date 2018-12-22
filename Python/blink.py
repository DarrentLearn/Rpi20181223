#!/home/pi/Documents/python/blink.py
from gpiozero import LED
from signal import pause

red = LED(25)
red.blink(0.2)

pause()