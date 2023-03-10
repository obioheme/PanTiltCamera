import RPi.GPIO as GPIO
import time

#Azimuth Control Pins
A_out1 = 17
A_out2 = 18
A_out3 = 23
A_out4 = 24

#Elevation Control Pins
E_out1 = 12
E_out2 = 16
E_out3 = 20
E_out4 = 21

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.02

step_count = 10

# setting up
GPIO.setmode(GPIO.BCM )
GPIO.setwarnings(False)
GPIO.setup(A_out1, GPIO.OUT)
GPIO.setup(A_out2, GPIO.OUT)
GPIO.setup(A_out3, GPIO.OUT)
GPIO.setup(A_out4, GPIO.OUT)

GPIO.setup(E_out1, GPIO.OUT)
GPIO.setup(E_out2, GPIO.OUT)
GPIO.setup(E_out3, GPIO.OUT)
GPIO.setup(E_out4, GPIO.OUT)


# initializing
GPIO.output(A_out1, GPIO.LOW)
GPIO.output(A_out2, GPIO.LOW)
GPIO.output(A_out3, GPIO.LOW)
GPIO.output(A_out4, GPIO.LOW)

GPIO.output(E_out1, GPIO.LOW)
GPIO.output(E_out2, GPIO.LOW)
GPIO.output(E_out3, GPIO.LOW)
GPIO.output(E_out4, GPIO.LOW)


def cleanup():
    GPIO.output(A_out1, GPIO.LOW)
    GPIO.output(A_out2, GPIO.LOW)
    GPIO.output(A_out3, GPIO.LOW)
    GPIO.output(A_out4, GPIO.LOW)
    
    GPIO.output(E_out1, GPIO.LOW)
    GPIO.output(E_out2, GPIO.LOW)
    GPIO.output(E_out3, GPIO.LOW)
    GPIO.output(E_out4, GPIO.LOW)
    GPIO.cleanup()


# the meat
def azimuth_clockwise():
    try:
        i = 0
        for i in range(step_count):
            if i%4==0:
                GPIO.output(A_out4, GPIO.HIGH)
                GPIO.output(A_out3, GPIO.LOW)
                GPIO.output(A_out2, GPIO.LOW)
                GPIO.output(A_out1, GPIO.LOW)
            elif i%4==1:
                GPIO.output(A_out4, GPIO.LOW)
                GPIO.output(A_out3, GPIO.LOW)
                GPIO.output(A_out2, GPIO.HIGH)
                GPIO.output(A_out1, GPIO.LOW)
            elif i%4==2:
                GPIO.output(A_out4, GPIO.LOW)
                GPIO.output(A_out3, GPIO.HIGH)
                GPIO.output(A_out2, GPIO.LOW)
                GPIO.output(A_out1, GPIO.LOW)
            elif i%4==3:
                GPIO.output(A_out4, GPIO.LOW)
                GPIO.output(A_out3, GPIO.LOW)
                GPIO.output(A_out2, GPIO.LOW)
                GPIO.output(A_out1, GPIO.HIGH)

            time.sleep(step_sleep)

    except KeyboardInterrupt:
        cleanup()
        exit(1)


def elevation_clockwise():
    try:
        i = 0
        for i in range(step_count):
            if i%4==0:
                GPIO.output(E_out4, GPIO.HIGH)
                GPIO.output(E_out3, GPIO.LOW)
                GPIO.output(E_out2, GPIO.LOW)
                GPIO.output(E_out1, GPIO.LOW)
            elif i%4==1:
                GPIO.output(E_out4, GPIO.LOW)
                GPIO.output(E_out3, GPIO.LOW)
                GPIO.output(E_out2, GPIO.HIGH)
                GPIO.output(E_out1, GPIO.LOW)
            elif i%4==2:
                GPIO.output(E_out4, GPIO.LOW)
                GPIO.output(E_out3, GPIO.HIGH)
                GPIO.output(E_out2, GPIO.LOW)
                GPIO.output(E_out1, GPIO.LOW)
            elif i%4==3:
                GPIO.output(E_out4, GPIO.LOW)
                GPIO.output(E_out3, GPIO.LOW)
                GPIO.output(E_out2, GPIO.LOW)
                GPIO.output(E_out1, GPIO.HIGH)

            time.sleep(step_sleep)

    except KeyboardInterrupt:
        cleanup()
        exit(1)


def azimuth_anti_clockwise():
    try:
        i = 0
        for i in range(step_count):
            if i%4==0:
                GPIO.output(A_out4, GPIO.LOW)
                GPIO.output(A_out3, GPIO.LOW)
                GPIO.output(A_out2, GPIO.LOW)
                GPIO.output(A_out1, GPIO.HIGH)
            elif i%4==1:
                GPIO.output(A_out4, GPIO.LOW)
                GPIO.output(A_out3, GPIO.HIGH)
                GPIO.output(A_out2, GPIO.LOW)
                GPIO.output(A_out1, GPIO.LOW)
            elif i%4==2:
                GPIO.output(A_out4, GPIO.LOW)
                GPIO.output(A_out3, GPIO.LOW)
                GPIO.output(A_out2, GPIO.HIGH)
                GPIO.output(A_out1, GPIO.LOW)
            elif i%4==3:
                GPIO.output(A_out4, GPIO.HIGH)
                GPIO.output(A_out3, GPIO.LOW)
                GPIO.output(A_out2, GPIO.LOW)
                GPIO.output(A_out1, GPIO.LOW)

            time.sleep( step_sleep )

    except KeyboardInterrupt:
        cleanup()
        exit( 1 )


def elevation_anti_clockwise():
    try:
        i = 0
        for i in range(step_count):
            if i%4==0:
                GPIO.output(E_out4, GPIO.LOW)
                GPIO.output(E_out3, GPIO.LOW)
                GPIO.output(E_out2, GPIO.LOW)
                GPIO.output(E_out1, GPIO.HIGH)
            elif i%4==1:
                GPIO.output(E_out4, GPIO.LOW)
                GPIO.output(E_out3, GPIO.HIGH)
                GPIO.output(E_out2, GPIO.LOW)
                GPIO.output(E_out1, GPIO.LOW)
            elif i%4==2:
                GPIO.output(E_out4, GPIO.LOW)
                GPIO.output(E_out3, GPIO.LOW)
                GPIO.output(E_out2, GPIO.HIGH)
                GPIO.output(E_out1, GPIO.LOW)
            elif i%4==3:
                GPIO.output(E_out4, GPIO.HIGH)
                GPIO.output(E_out3, GPIO.LOW)
                GPIO.output(E_out2, GPIO.LOW)
                GPIO.output(E_out1, GPIO.LOW)

            time.sleep(step_sleep)

    except KeyboardInterrupt:
        cleanup()
        exit(1)
