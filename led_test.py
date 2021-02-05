import RPi.GPIO as GPIO
import time
from random import randint

print 'Controlling LED test'
led_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        print ("turn on led")
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(randint(3,10))
        print("turn off led")
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.cleanup()

print('done.')


