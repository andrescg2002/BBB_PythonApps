'''
We know that when the potentiometer reads 0, we want a 0% duty cycle on the PWM pin, which would have the LED off. This is our first point:
(0,0)

We also know that when we read 1 from the potentiometer, we want to apply a duty cycle of 100%, or have the LED be full bright. This is our second point:
(1,100)

If we created an equation for the line between these two points, we could calculate the duty cycle that should be applied based on the potentiometer reading. 
The problem with this is the way our eye perceives changes in brightness. We perceive exponential changes, so if we connected the two points with a linear
relationship we would see lots of change at the low end of the scale, but as we continued to move the potentiometer, the brightness would appear to saturate. 
In order to have a nice smooth transition from full dim to full bright as the potentiometer is moved from left to right, we need to fit an exponential curve
between the two points above. We want the LED to be off when the pot is full left, and full bright when the pot is fully to the right. We could use the 
exponential equation: DC = C^(analogRead) - B. Replace the 2 points above to know C and B constants

- See more at: http://www.toptechboy.com/beaglevone-black-rev-c/beaglebone-black-lesson-10-dimable-led-using-potentiometer/#sthash.vBjcbVMV.dpuf
'''

import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC
from time import sleep

adcPin = "P9_33"
led = "P9_14"

ADC.setup()
PWM.start(led, 0, 1000)

while(1):
    analogRead = ADC.read(adcPin)
    #DC = C^(analogRead) - B
    dutyCycle = 101**(analogRead) -1
    PWM.set_duty_cycle(led, dutyCycle)
    sleep(0.5)
    
print ("Program End")
    

    