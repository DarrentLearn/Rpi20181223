from gpiozero import PWMLED, MCP3008, RGBLED,Button
from signal import pause
import random
from time import sleep

def btnPressed():
    global r, rTemp, g, gTemp, b, bTemp
    r =random.randint(0, 100)
    rTemp=r
    g=random.randint(0, 100)
    gTemp=g
    b=random.randint(0, 100)
    bTemp=b
    print("btnPressed, r={},rT={},g={},gT={},b={},bT={}".format(r,rTemp,g,gTemp,b,bTemp))
    sleep(3)

btn = Button(27)
led = PWMLED(4)
pot = MCP3008(channel=7)
rgbLed = RGBLED(16,20,21)

led.source = pot.values

btn.when_pressed= btnPressed

r=0
g=0
b=0
rTemp=0
gTemp=0
bTemp=0

while True:
    if r > rTemp:
        r -= 1
    elif r < rTemp:
        r += 1
    else:
        rTemp = random.randint(0, 100)
    if g > gTemp:
        g -= 1
    elif g < gTemp:
        g += 1
    else:
        gTemp = random.randint(0, 100)
    if b > bTemp:
        b -= 1
    elif b < bTemp:
        b += 1
    else:
        bTemp = random.randint(0, 100 )
    print("r={},rT={},g={},gT={},b={},bT={}".format(r,rTemp,g,gTemp,b,bTemp))
    rgbLed.color=(r/100,g/100,b/100)
    sleep(0.1)

#pause()

