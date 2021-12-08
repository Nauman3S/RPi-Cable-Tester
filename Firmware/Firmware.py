import time
import RPi.GPIO as GPIO

Connector1Pins = [4, 17, 27, 22, 10, 9]  # output pins
Connector2Pins = [11, 5, 6, 13, 19, 26]  # input pins
Connector3Pins = [18, 23, 24, 25, 8, 7]  # input pins

correctConnections = [0, 0, 0, 0, 0, 0]

LEDPin = 12  # GPIO12



GPIO.setmode(GPIO.BCM)  # BCM pin-numbering (GPIOs)

GPIO.setup(LEDPin, GPIO.OUT)
GPIO.output(LEDPin, GPIO.LOW)
for i in range(0, len(Connector1Pins)):

    GPIO.setup(Connector1Pins[i], GPIO.OUT)
    GPIO.output(Connector1Pins[i], GPIO.LOW)


for i in range(0, len(Connector1Pins)):

    #using internal pull-up
    GPIO.setup(Connector2Pins[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #using internal pull-up
    GPIO.setup(Connector3Pins[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def checkAllConnections():
    global correctConnections
    correctC=0
    for i in range(0, len(correctConnections)):
        if(correctConnections[i]==1):
            correctC=correctC+1
    if(correctC>=6):
        return 1
    else:
        return 0

try:
    while 1:
        for pinIndex in range (0,len(correctConnections)):
            if (GPIO.input(Connector2Pins[pinIndex]) == 0 and GPIO.input(Connector3Pins[pinIndex])==0): 
                correctConnections[pinIndex]=1
            else:
                correctConnections[pinIndex]=0

        if(checkAllConnections()==1):#check if all the connections are working
            GPIO.output(LEDPin, GPIO.HIGH)
        else:
            GPIO.output(LEDPin, GPIO.LOW)

        time.sleep(0.5)
        # print(correctConnections)
   
except KeyboardInterrupt:  # exit on CTRL+C
    GPIO.cleanup() 
    print(correctConnections)
