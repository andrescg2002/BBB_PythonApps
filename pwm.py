import Adafruit_BBIO.PWM as PWM
myPWM = "P8_13"


#Pin, duty_cycle, frequency
PWM.start(myPWM, 0, 1000)

for i in range(0, 5):
    DC = input("What duty_cycle do you like? ")
    if DC > 100:
        DC = 100
        
    PWM.set_duty_cycle(myPWM, DC)
    
PWM.stop(myPWM)
PWM.cleanup()
        