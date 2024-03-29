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
    duty = (angle + 90
            ) / 18 + 2
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
    for angle in range(-90, 91, 10):
        set_angle(pan_pin, angle)
        time.sleep(0)

    # Perform auto-scan from right to left
    for angle in range(90, -91, -10):
        set_angle(pan_pin, angle)
        time.sleep(0)
        
    # Perform auto-scan from up to down
    for angle in range(-90, 91, 10):
        set_angle(tilt_pin, angle)
        time.sleep(0)

    # Perform auto-scan from down to up
    for angle in range(90, -91, -10):
        set_angle(tilt_pin, angle)
        time.sleep(0)

# Function to stop motor at the current angle
def stop_motor():
    current_pan_angle = 0  # Get the actual current angle (you need to implement this)
    current_tilt_angle = 0  # Get the actual current angle (you need to implement this)
    
    set_angle(pan_pin, current_pan_angle)
    set_angle(tilt_pin, current_tilt_angle)

# Function to stop motor at the current angle
def reset_motor():
    current_pan_angle = 0  # Get the actual current angle (you need to implement this)
    current_tilt_angle = 0  # Get the actual current angle (you need to implement this)
    
    set_angle(pan_pin, current_pan_angle)
    set_angle(tilt_pin, current_tilt_angle)
    
def start_scan():
    # Perform auto-scan every 30 seconds
    auto_scan()
    time.sleep(30)  # 30 seconds

def pan_turn_clockwise():
    for angle in range(-90, 91, 10):  
        set_angle(pan_pin, angle)

def pan_turn_anticlockwise():
    for angle in range(90, -91, 10): 
        set_angle(pan_pin, angle)

def tilt_turn_clockwise():
    for angle in range(-90, 91, 10):  
        set_angle(tilt_pin, angle)

def tilt_turn_anticlockwise():
    for angle in range(90, -91, 10): 
        set_angle(tilt_pin, angle)

start_scan()
