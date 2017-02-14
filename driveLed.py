import Adafruit_BBIO.GPIO as GPIO
from time import sleep
LEDTop = "P9_12"
LEDBottom = "P9_11"

GPIO.setup(LEDTop,GPIO.OUT)
GPIO.setup(LEDBottom,GPIO.OUT)

for i in range(0,5):
        GPIO.output(LEDTop,GPIO.HIGH)
        GPIO.output(LEDBottom,GPIO.HIGH)
        sleep(1)
        GPIO.output(LEDTop,GPIO.LOW)
        GPIO.output(LEDBottom,GPIO.LOW)
        sleep(1)

print "AppEnd" 
GPIO.cleanup()


        