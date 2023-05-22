# Import all relevant libraries here
from time import sleep
from gpiozero import DistanceSensor, LED

#Define the GPIO pin numbers for the trigger and echo pins
GreenLED = LED(26)
RedLED = LED(6)
Ultrasonicsensor = DistanceSensor(echo=21,trigger=20)

#Define safe distance
safe_distance = 2 # Assuming Meters

def main():
    print("Starting Script")
    GreenLED.off()
    while True:
    #Measure the distance and print the value in centimeters
        distance = Ultrasonicsensor.distance
       # if round(distance,2) < safe_distance:
          # GreenLED.off()
          # RedLED.on()
       # elif round(distance,2) >= safe_distance:
          # RedLED.off()
          # GreenLED.on()
        print("Distance {:.2f} m".format(distance))
        #Wait for 1 second before taking the nextmeasurement
        pause()

if __name__ == "__main__":
    main()
