# Import all relevant libraries here
from time import sleep
from gpiozero import DistanceSensor, LED

#Define the GPIO pin numbers for the trigger and echo pins
green = LED(26)
red = LED(19)
sensor = DistanceSensor(echo=21, trigger=20, max_distance=6)

#Define safe distance
safe_distance = 1 # Assuming Meters

def main():
    print("Starting Script")
    while True:
        #Measure the distance and print the value in centimeters
        distance = sensor.distance
        print(distance,"\n")
        if distance > safe_distance:
           green.on()
           red.off()
        elif distance < safe_distance:
           red.on()
           green.off()
        #Wait for 1 second before taking the next measurement
        sleep(1)

if __name__ == "__main__":
    main()