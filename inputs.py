import Adafruit_BBIO.GPIO as GPIO
from time import sleep

topButton = "P9_11"
bottomButton = "P9_13"

GPIO.setup(topButton, GPIO.IN)
GPIO.setup(bottomButton, GPIO.IN)

while(1):
    if (GPIO.input(topButton)):
        print ("Top Button pressed")
        
    if (GPIO.input(bottomButton)):
        print ("Bottom Button pressed")
        
    if (GPIO.input(topButton) and GPIO.input(bottomButton)):
        break;
        
    sleep(0.2)

print ("Program ended")    
GPIO.cleanup    
    
