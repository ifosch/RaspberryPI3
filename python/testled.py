import RPi.GPIO as GPIO
import sys
import time
import signal


def handler(signum, frame):

    GPIO.cleanup()

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGTERM, handler)


value = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.IN)
GPIO.output(17,False)
lastchange = value
while (True):
    #try :
	value = GPIO.input(27)
	if value and not lastchange:
            ledvalue = not ledvalue
	    GPIO.output(17, ledvalue)
    	lastchange = value
        time.sleep(0.02)
    #except (KeyboardInterrupt ):
    # 	GPIO.cleanup()
    #  	break
