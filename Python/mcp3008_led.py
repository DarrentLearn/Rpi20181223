import time
import pigpio
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

SPI_PORT   = 0
SPI_DEVICE = 0

SIGNAL_CHANNEL = 0
PWM_LED_PIN = 18
PWM_FREQ = 800

mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
pi = pigpio.pi()

try:
    print('按下 Ctrl-C 可停止程式')
    while True:
        switch_value = mcp.read_adc(SIGNAL_CHANNEL)
        print(switch_value)
        pi.hardware_PWM(PWM_LED_PIN, PWM_FREQ, int(switch_value/1023*1000000))
        time.sleep(0.1)
except KeyboardInterrupt:
    print('關閉程式')
finally:
    pi.set_mode(PWM_LED_PIN, pigpio.INPUT)