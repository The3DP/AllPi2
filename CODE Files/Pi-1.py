import RPi.GPIO as GPIO
import time
import sys

# === CONFIG ===
FAN_PIN = 18  # GPIO pin (PWM capable)
FREQ = 25000  # PWM frequency in Hz

# === Setup ===
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)
fan_pwm = GPIO.PWM(FAN_PIN, FREQ)
fan_pwm.start(0)  # Start with fan off

try:
    if len(sys.argv) != 2:
        print("Usage: sudo python3 fan_control.py <speed_percent>")
        print("Example: sudo python3 fan_control.py 75")
        sys.exit(1)

    speed = int(sys.argv[1])
    if not 0 <= speed <= 100:
        print("Speed must be between 0 and 100")
        sys.exit(1)

    fan_pwm.ChangeDutyCycle(speed)
    print(f"Fan speed set to {speed}%")

    # Keep it running for a bit (optional)
    time.sleep(5)

finally:
    fan_pwm.stop()
    GPIO.cleanup()
