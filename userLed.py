import sys

LED3_PATH = "/sys/class/leds/beaglebone:green:usr3"

def writeLed (filename, value, path = LED3_PATH):
    #This function writes the passed value to the file in the path
    file = open(path + filename, "w")
    file.write(value)
    file.close()
    return

def removeTrigger():
    writeLed("/trigger","none")
    return

print ("Starting the Led python script")

if len(sys.argv) != 2:
    print ("There are an incorrect number of arguments")
    print (" usage is: userLed.py command")
    print (" where command is one of on, off, flash or status")
    sys.exit(2)
    
if sys.argv[1] == "on":
    print ("Turning the led on")
    removeTrigger()
    writeLed("/brightness", "1")
    
elif sys.argv[1] == "off":
    print ("Turning the led off")
    removeTrigger()
    writeLed("/brightness", "0")
    
elif sys.argv[1] == "flash":
    print ("Flashing the led")
    removeTrigger()
    writeLed("/trigger", "timer")    
    writeLed("/delay_on", "50")
    writeLed("/delay_off", "50")
    
elif sys.argv[1] == "status":
    print ("Getting the led trigger status")
    file = open(LED3_PATH + "/trigger", "r")
    print (file.read())
    file.close()

else:
    print ("Invalid command")
    
print ("End of python script")
    
    
    