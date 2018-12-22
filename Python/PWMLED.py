#!/home/pi/Documents/python/PWMLED.py
from gpiozero import PWMLED
from time import sleep

led = PWMLED(25)

# while True:
#     led.value = 0  # off
  #   sleep(1)
  #   led.value = 0.3  # half brightness
  #   sleep(1)
  #   led.value = 1  # full brightness
  #   sleep(1)
    

while True:
    for num in range(0,10,1):
        led.value = num/10
        print(led.value)
        sleep(0.1)
    sleep(0.3)
    for num in range(9,0,-1):
        led.value = num/10
        print(led.value)
        sleep(0.1)
    sleep(0.3)
    