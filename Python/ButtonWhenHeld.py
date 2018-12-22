from gpiozero import LEDBoard
from gpiozero import Button, LED
from signal import pause
from time import sleep
   
def Action():
    leds.Red.on()
    sleep(1)
    leds.Red.off()
    leds.Green.on()
    sleep(1)
    leds.Green.off()
    leds.Blue.on()
    sleep(1)
    leds.Blue.off()

leds = LEDBoard(Red=5, Green=6, Blue=13)
button = Button(17, hold_time=2)

button.when_held = Action
pause()


        

    
