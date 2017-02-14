import Adafruit_BBIO.ADC as ADC
ADC.setup()

from time import time
from time import sleep

analogPin = "P9_33"
#Current time in seconds 
refTime = time()


while(time() - refTime < 30):
    portVal = ADC.read(analogPin)
    voltage = portVal * 1.8
    print ("Voltage on adc pin is %1.3f" % (voltage))
    sleep(0.5)
    #print ("Time to end the program ", (time() - refTime))
    '''
    newRead = raw_input("Do you want to continue reading? (y/n) ")
    if (newRead == 'y'):
        continue
    else:
        break
    '''
        
print ("Program ended")

        
    
    
    