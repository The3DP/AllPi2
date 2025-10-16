# The following code is a GPIO test (single port) connected to GPIO 18

import RPi.GPIO as GPIO
import time

# Constants
PIN = 18  # GPIO 18 (pin 12 on the board)
BLINKS = 5
DELAY = 0.5  # seconds

def gpio_test():
    GPIO.setmode(GPIO.BCM)  # Use BCM numbering
    GPIO.setup(PIN, GPIO.OUT)

    print(f"Testing GPIO {PIN} by blinking an LED {BLINKS} times...")

    try:
        for i in range(BLINKS):
            print(f"Blink {i+1}")
            GPIO.output(PIN, GPIO.HIGH)
            time.sleep(DELAY)
            GPIO.output(PIN, GPIO.LOW)
            time.sleep(DELAY)

        print("Test complete.")

    except KeyboardInterrupt:
        print("Test interrupted by user.")

    finally:
        GPIO.cleanup()
        print("GPIO cleaned up.")

if __name__ == "__main__":
    gpio_test()
