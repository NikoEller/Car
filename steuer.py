import RPi.GPIO as GPIO
from time import sleep
import time

a = ""

GPIO.setmode(GPIO.BOARD)

Motor1A = 16
Motor1B = 18
Motor1E = 22

Motor2A = 23
Motor2B = 21
Motor2E = 19

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




def stop():
    #print("Now stop")
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)
    GPIO.cleanup()




def distance():
    # setze Trigger auf HIGH
    GPIO.output(GPIO_TRIGGER2, True)

    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER2, False)

    StartZeit2 = time.time()
    StopZeit2 = time.time()

    # speichere Startzeit
    while GPIO.input(GPIO_ECHO2) == 0:
        StartZeit2 = time.time()

    # speichere Ankunftszeit
    while GPIO.input(GPIO_ECHO2) == 1:
        StopZeit2 = time.time()

    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed2 = StopZeit2 - StartZeit2
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    distanz2 = (TimeElapsed2 * 34300) / 2

    GPIO.setmode(GPIO.BOARD)

    print(distanz2)



if __name__ == '__main__':
    try:
        while True:
            a = raw_input()
            if(a == "w"):
                abstandok()
                goforward()
                distance()
            if(a == "a"):
                abstandok()
                turn()
                distance()
            if(a == "d"):
                abstandok()
                turn1()
                distance()
            if(a == "p"):
                abstandok()
                distance()
                stop()

                break

        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
