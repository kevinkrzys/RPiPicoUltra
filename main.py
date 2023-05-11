# Import all relevant libraries

from machine import Pin, time_pulse_us
from time import sleep_us, sleep

# Define the GPIO pin numbers for the trigger and echo pins
TRIGGER_PIN = 27
ECHO_PIN = 26
RED_LED_PIN = 21
GREEN_LED_PIN = 17

# Initialize trigger and echo pins
trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)
red_led = Pin(RED_LED_PIN, Pin.OUT)
green_led = Pin(GREEN_LED_PIN, Pin.OUT)

# Define safe distance
safe_distance = 200

def measure_distance():
    # Ensure trigger is low initially
    trigger.low()
    sleep_us(2)

    # Send a 10 microsecond pulse to the trigger pin
    trigger.high()
    sleep_us(10)
    trigger.low()

    # Measure the duration of the echo pulse (in microseconds)
    pulse_duration = time_pulse_us(echo, Pin.high)

    # Calculate the distance (in centimeters) using the speed of sound (343 m/s)
    distance = pulse_duration * 0.0343 / 2
    return distance

def main():
    green_led.on()
    while True:
        # Measure the distance and print the value in centimeters
        distance = measure_distance()
        if round(distance,2) < safe_distance:
            green_led.off()
            red_led.on()
        elif round(distance,2) >= safe_distance:
            red_led.off()
            green_led.on()
        # print("Distance: {:.2f} cm".format(distance))
        
        # Wait for 1 second before taking the next measurement
        sleep(1)

if __name__ == "__main__":
    main()
