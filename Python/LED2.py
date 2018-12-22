from gpiozero import LED
from time import sleep
from gpiozero import Button
from signal import pause

button = Button(17)
led = LED(27)

button.when_pressed = led.on
button.when_released = led.off
pause()
    
#while True:    
    #if button.is_pressed:
    #    print("Pressed")
    #    led.on()
    #else:
    #    print("Released")
    #    led.off()
    #sleep(0.1)

