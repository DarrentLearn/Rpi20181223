from gpiozero import LEDBoard
from gpiozero import Button, LED
from signal import pause
from time import sleep
   
def Action():
    timer.cancel()
    leds.Red.on()
    sleep(1)
    leds.Red.off()
    leds.Green.on()
    sleep(1)
    leds.Green.off()
    leds.Blue.on()
    sleep(1)
    leds.Blue.off()

def userPressed():
    print("pressed")
    Action()
    #led.on();
    
    #led.toggle();

def userReleased():
    print("released")
    timer.cancel()
    #led.off();

timer = threading.Timer(2.0, Action)


leds = LEDBoard(Red=5, Green=6, Blue=13)
button = Button(17, hold_time=2)

button.when_pressed = userPressed
button.when_released = userReleased
pause()


        

    