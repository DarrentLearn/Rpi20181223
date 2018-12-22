import RPi.GPIO as GPIO
import time

LED_PIN = 21
PWM_FREQ = 200

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, PWM_FREQ)
pwm.start(0)

try:
    print('按下 Ctrl-C 可停止程式')
    while True:
        for duty_cycle in range(0, 20, 1):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.2)
        for duty_cycle in range(20, 0, -1):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.2)
except KeyboardInterrupt:
    print('關閉程式')
finally:
    pwm.stop()
    GPIO.cleanup()