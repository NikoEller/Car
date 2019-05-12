import RPi.GPIO as GPIO
from time import sleep
import time
import socket

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
GPIO_TRIGGER2 = 17
GPIO_ECHO2 = 4

# Richtung der GPIO-Pins festlegen (IN / OUT)S
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)


def goforward():
    # print("Going forwards")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

    sleep(1)
    # print("Now stop")
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
    # print("Going left")
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

    sleep(1)
    # print("Now stop")
    GPIO.output(Motor2E, GPIO.LOW)


def turn1():
    # print("Going forwards")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    sleep(1)
    # print("Now stop")
    GPIO.output(Motor1E, GPIO.LOW)

def roundturn():
    # print("Going forwards")
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

    sleep(1)
    # print("Now stop")
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)


def stop():
    # print("Now stop")
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

    print(distanz2)


if __name__ == '__main__':
    try:
        HOST = '192.168.2.118'  # The remote host
        PORT = 50007  # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall('Hello, world!')
        while True:
            data = s.recv(1024)
            if (data == 'w'):
                goforward()
            if (data == "a"):
                turn()
            if (data == "d"):
                turn1()
            if (data == "s"):
                backwards()
            if (data == "p"):
                roundturn()




        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("")
        s.close
        GPIO.cleanup()
