import RPi.GPIO as IO
import time

senvenLed = (17,4,23,24,25,27,22,18)
font = {
    0:(1, 1, 1, 1, 1, 1, 0, 0),
    1:(0, 1, 1, 0, 0, 0, 0, 0),
    2:(1, 1, 0, 1, 1, 0, 1, 0),
    3:(1, 1, 1, 1, 0, 0, 1, 0),
    4:(0, 1, 1, 0, 0, 1, 1, 0),
    5:(1, 0, 1, 1, 0, 1, 1, 0),
    6:(1, 0, 1, 1, 1, 1, 1, 0),
    7:(1, 1, 1, 0, 0, 1, 0, 0),
    8:(1, 1, 1, 1, 1, 1, 1, 0),
    9:(1, 1, 1, 0, 0, 1, 1, 0),
    10:(0,0,0,0,0,0,0,0),
    }
phoneNumber = (9,6,3,6,3,0,2,5,10)

IO.setwarnings(False)
IO.setmode(IO.BCM)
for x in senvenLed:
    IO.setup(x,IO.OUT)
    
#for x in senvenLed:
#    print(x)
#    IO.output(x, IO.HIGH)
#    time.sleep(1)
#    IO.output(x, IO.LOW)
#time.sleep(5)

while True:
    for n in phoneNumber:
        nv = font[n]
        i = 0
        for p in senvenLed:
            IO.output(p,nv[i])
            i += 1
        time.sleep(1)
        i = 0
        nv = font[10]
        for p in senvenLed:
            IO.output(p,nv[i])
            i += 1
        time.sleep(0.1)

