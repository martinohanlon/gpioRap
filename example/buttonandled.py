import gpioRap as gpioRap
import RPi.GPIO as GPIO

print "An example of gpioRap, when the button is pressed it will light the led, and pressed again it will turn off the led"

#Create GpioRap class using BCM pin numbers
gpioRapper = gpioRap.GpioRap(GPIO.BCM)

#Create an LED, which should be attached to pin 17
led = gpioRapper.createLED(17)
#Create a button, which should be monitored by pin 4, where a False is read when the button is pressed
button = gpioRapper.createButton(4, False)
try:
        #Loop
        while True:
                #Wait for the button to be pressed
                if button.waitForPress(3) == True:
                        led.toggle()

except KeyboardInterrupt:
        #Cleanup
        gpioRapper.cleanup()
