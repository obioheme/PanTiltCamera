import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.OUT) # IN1
GPIO.setup(11, GPIO.OUT) # IN2
GPIO.setup(15, GPIO.OUT) # IN3
GPIO.setup(12, GPIO.OUT) # IN4
GPIO.setup(16, GPIO.OUT) # IN1 for second motor
GPIO.setup(18, GPIO.OUT) # IN2 for second motor
GPIO.setup(22, GPIO.OUT) # IN3 for second motor
GPIO.setup(24, GPIO.OUT) # IN4 for second motor

# Define stepper motor sequence
sequence = [[1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]]

# Function to control stepper motor
def step(steps, direction, motor):
    if motor == 1:
        IN1 = 13
        IN2 = 11
        IN3 = 15
        IN4 = 12
    elif motor == 2:
        IN1 = 16
        IN2 = 18
        IN3 = 22
        IN4 = 24
    for i in range(steps):
        for j in range(8):
            GPIO.output(IN1, sequence[j][0])
            GPIO.output(IN2, sequence[j][1])
            GPIO.output(IN3, sequence[j][2])
            GPIO.output(IN4, sequence[j][3])
            time.sleep(0.001)
    if direction == "CW":
        print("Motor {} moved {} steps clockwise".format(motor, steps))
    elif direction == "CCW":
        print("Motor {} moved {} steps counterclockwise".format(motor, steps))
    else:
        print("Invalid direction")

# Control motors
while True:
    command = input("Enter command (Motor1, Motor2, Stop): ")
    if command == "Motor1":
        direction = input("Enter direction (CW, CCW): ")
        steps = int(input("Enter steps: "))
        step(steps, direction, 1)
    elif command == "Motor2":
        direction = input("Enter direction (CW, CCW): ")
        steps = int(input("Enter steps: "))
        step(steps, direction, 2)
    elif command == "Stop":
        break
    else:
        print("Invalid command")

# Clean up GPIO pins
GPIO.cleanup()
