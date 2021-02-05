from device.led_light import LED
import time

red_led = LED(pin=17)

for i in range(10):
    red_led.turn_on()
    time.sleep(3)
    red_led.turn_off()
    time.sleep(3)
