import RPi.GPIO as GPIO
from time import sleep
import time

a = ""

GPIO.setmode(GPIO.BCM)

Motor1A = 23
Motor1B = 24
Motor1E = 25

Motor2A = 11
Motor2B = 9
Motor2E = 10

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

# GPIO Pins dem Ultraschallsensor 2 zuweisen
GPIO_TRIGGER2 = 11
GPIO_ECHO2 = 7

# Richtung der GPIO-Pins festlegen (IN / OUT)S
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)


def goforward():
    #print("Going forwards")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

    sleep(1)
    #print("Now stop")
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)

def backwards():
    # print("Going forwards")
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)

    sleep(1)
    # print("Now stop")
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)




def turn():
    #print("Going left")
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

    sleep(1)
    #print("Now stop")
    GPIO.output(Motor2E, GPIO.LOW)

def turn1():
    #print("Going forwards")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    sleep(1)
    #print("Now stop")
    GPIO.output(Motor1E, GPIO.LOW)


def doubleturn():
    # print("Going forwards")
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    sleep(1)
    GPIO.output(Motor1E, GPIO.LOW)

    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

    sleep(1)
    # print("Now stop")

    GPIO.output(Motor2E, GPIO.LOW)





def stop():
    #print("Now stop")
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)
    GPIO.cleanup()



if __name__ == '__main__':
    try:
        while True:
            a = raw_input()
            if(a == "w"):
                goforward()
            if(a == "a"):
                turn()
            if(a == "d"):
                turn1()
            if(a == "s"):
                backwards()
            if(a == "p"):
                stop()
                break
            if(a == "e"):
                doubleturn()



        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("")
        GPIO.cleanup()
