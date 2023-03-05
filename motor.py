#import RPi.GPIO as GPIO
#from RPiMotorLib import RPiMotorLib
#import time

#Azimuth Motor Control Pins
A_out1 = 15
A_out2 = 18
A_out3 = 23
A_out4 = 24

step_sleep = 0.003
step_count = 10
i = 0

#Elevation Motor Control Pins
E_out1 = 12
E_out2 = 16
E_out3 = 20
E_out4 = 21

#Setting Up GPIO Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(A_out1, GPIO.OUT)
GPIO.setup(A_out2, GPIO.OUT)
GPIO.setup(A_out3, GPIO.OUT)
GPIO.setup(A_out4, GPIO.OUT)

GPIO.setup(E_out1, GPIO.OUT)
GPIO.setup(E_out2, GPIO.OUT)
GPIO.setup(E_out3, GPIO.OUT)
GPIO.setup(E_out4, GPIO.OUT)

#Initializing GPIO Pins
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


#Clockwise Sequence for Motor Control
sequence = [[1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1]
            [0, 0, 0, 1]]

#Anti-Clockwise Sequence for Motor Control
anti_sequence = [[0, 0, 0, 1]
                 [0, 0, 1, 1]
                 [0, 0, 1, 0]
                 [0, 1, 1, 0]
                 [0, 1, 0, 0]
                 [1, 1, 0, 0]
                 [1, 0, 0, 0]
                 [1, 0, 0, 1]]


#Azimuth Motor Control
def azimuth_clockwise():
    for i in range(step_count):
        for j in range(8):
            GPIO.output(A_out1, sequence[j][0])
            GPIO.output(A_out2, sequence[j][1])
            GPIO.output(A_out3, sequence[j][2])
            GPIO.output(A_out4, sequence[j][3])
            time.sleep(0.001)


def azimuth_anti_clockwise():
    for i in range(step_count):
        for j in range(8):
            GPIO.output(A_out1, anti_sequence[j][0])
            GPIO.output(A_out2, anti_sequence[j][1])
            GPIO.output(A_out3, anti_sequence[j][2])
            GPIO.output(A_out4, anti_sequence[j][3])


#Elevation Motor Control
def elevation_clockwise():
    for i in range(step_count):
        for j in range(8):
            GPIO.output(E_out1, sequence[j][0])
            GPIO.output(E_out2, sequence[j][1])
            GPIO.output(E_out3, sequence[j][2])
            GPIO.output(E_out4, sequence[j][3])


def elevation_anti_clockwise():
    for i in range(step_count):
        for j in range(8):
            GPIO.output(E_out1, anti_sequence[j][0])
            GPIO.output(E_out2, anti_sequence[j][1])
            GPIO.output(E_out3, anti_sequence[j][2])
            GPIO.output(E_out4, anti_sequence[j][3])
