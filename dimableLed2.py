'''
We will want a press of the top button to increase brightness and a pres of the bottom button to decrease brightness. 
We want to insrease and decrease PWM signal exponentially, as this will allow the eye to perceive a smooth and linear increase in brightness.

If we want the LED to go from full off to full brightness in 10 steps, we need an equation to relate Duty Cycle to BP. 
BP will be a variable that will keep track of where we are. If we press the up button we increment BP by 1. 
If we press the down button, we decrements BP by 1. We want to start with BP=0, and the LED full off. This would be the point:

(BP,DutyCycle) = (0,0)

When the button has been pressed 10 times, we want a DutyCycle of 100%. This would be the point:

(BP,DutyCycle) = (10,100)

We now need to fit an exponential curve through these two points.

DC = C^(BP) -B

Replace the 2 points above to know C and B constants


- See more at: http://www.toptechboy.com/beaglevone-black-rev-c/beaglebone-black-lesson-11-dimable-led-with-buttons-from-python/#sthash.KIMI1KYz.dpuf
'''

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from time import sleep

topButton = "P9_23"
bottomButton = "P9_27"
led = "P9_14"

PWM.start(led, 0, 1000)
GPIO.setup(topButton, GPIO.IN)
GPIO.setup(bottomButton, GPIO.IN)
BP = 0

while(1):
    if (GPIO.input(topButton)):
        print ("Top Button pressed")
        BP = BP + 1
        
    if (GPIO.input(bottomButton)):
        print ("Bottom Button pressed")
        BP = BP - 1
        
    if(BP > 10):
        BP = 10
        
    if(BP < 0):
        BP = 0
    
    #DC = C^(BP) -B
    DC = 1.5864**(BP) - 1
    print "Duty Cycle ", DC
    PWM.set_duty_cycle(led, DC)
    sleep(0.5)
    
    
        
        

