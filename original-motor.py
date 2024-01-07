import RPi.GPIO as GPIO
import time

# GPIO pins for servo motors
pan_pin = 18  # GPIO pin for pan servo
tilt_pin = 23  # GPIO pin for tilt servo

# Set GPIO mode and setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pan_pin, GPIO.OUT)
GPIO.setup(tilt_pin, GPIO.OUT)

# Function to set servo angle
def set_angle(pin, angle):
    duty = (angle + 90) / 18 + 2
    GPIO.output(pin, True)
    pwm = GPIO.PWM(pin, 50)
    pwm.start(0)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    pwm.stop()
    GPIO.output(pin, False)

# Function to perform auto-scan
def auto_scan():
    # Perform auto-scan from left to right
    for angle in range(-90, 91, 20):
        set_angle(pan_pin, angle)
        time.sleep(0)

    # Perform auto-scan from right to left
    for angle in range(90, -91, -20):
        set_angle(pan_pin, angle)
        time.sleep(0)

    # Perform auto-scan from down to up
    for angle in range(-90, 91, 10):
        set_angle(tilt_pin, angle)
        time.sleep(0.5)

    # Perform auto-scan from up to down
    for angle in range(90, -91, -10):
        set_angle(tilt_pin, angle)
        time.sleep(0.5)

# Main loop
try:
    while True:
        # Perform auto-scan every 5 minutes
        auto_scan()
        time.sleep(60)  # 5 minutes
except KeyboardInterrupt:
    pass
finally:
    # Cleanup
    GPIO.cleanup()



