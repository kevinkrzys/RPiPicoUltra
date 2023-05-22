# Import all relevant libraries here
from time import sleep
from gpiozero import DistanceSensor, LED

#Define the GPIO pin numbers for the trigger and echo pins
GreenLED = LED(7)
RedLED = LED(25)
UltrasonicSensor = DistanceSensor(echo=21, trigger=12)

#Define safe distance
#safe_distance = 2 # Assuming Meters

def main():
    print("Starting Script")
    #GreenLED.on()
    #GreenLED.off()
    #RedLED.on()
    #REdLED.off()
    while True:
        #Measure the distance and print the value in centimeters
        distance = UltrasonicSensor.distance
        print(distance,"\n")
            #if distance < safe_distance:
                #GreenLED.off()
                #RedLED.on()
            #elif distance >= safe_distance:
                #RedLED.off()
                #GreenLED.on ()
            #print("Distance {:.2f} m".format(distance))
        #Wait for 1 second before taking the nextmeasurement
        sleep(1)

if __name__ == "__main__":
    main()
          