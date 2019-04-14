import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setmode(GPIO.BCM)

i = 0
tausender = 0
hunderter = 0
zehner = 0
einer = 0
distance1 = 0
Display0 = 5
Display1 = 12
Display2 = 21
Display3 = 26
A = 6
B = 7
C = 8
D = 13
E = 16
F = 19
G = 20

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


GPIO.setup(Display0, GPIO.OUT)
GPIO.setup(Display1, GPIO.OUT)
GPIO.setup(Display2, GPIO.OUT)
GPIO.setup(Display3, GPIO.OUT)
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)




def goforward():
    #print("Going forwards")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

    

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




    #__________________SEG7__________________________


def ultraschallsensor():
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
    distance1 = (TimeElapsed2 * 34300) / 2

    return distance1



def reset():
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    GPIO.output(E, GPIO.LOW)
    GPIO.output(F, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)


def a():
    GPIO.output(A, GPIO.HIGH)

def b():
    GPIO.output(B, GPIO.HIGH)

def c():
    GPIO.output(C, GPIO.HIGH)

def d():
    GPIO.output(D, GPIO.HIGH)

def e():
    GPIO.output(E, GPIO.HIGH)

def f():
    GPIO.output(F, GPIO.HIGH)

def g():
    GPIO.output(G, GPIO.HIGH)


def an():
    GPIO.output(A, GPIO.LOW)

def bn():
    GPIO.output(B, GPIO.LOW)

def cn():
    GPIO.output(C, GPIO.LOW)

def dn():
    GPIO.output(D, GPIO.LOW)

def en():
    GPIO.output(E, GPIO.LOW)

def fn():
    GPIO.output(F, GPIO.LOW)

def gn():
    GPIO.output(G, GPIO.LOW)




def one():
    an()
    b()
    c()
    dn()
    en()
    fn()
    gn()

def two():
    a()
    b()
    cn()
    d()
    e()
    fn()
    g()

def three():
    a()
    b()
    c()
    d()
    en()
    fn()
    g()

def four():
    an()
    b()
    c()
    dn()
    en()
    f()
    g()

def five():
    a()
    bn()
    c()
    d()
    en()
    f()
    g()

def six():
    an()
    bn()
    c()
    d()
    e()
    f()
    g()

def seven():
    a()
    b()
    c()
    dn()
    en()
    fn()
    gn()

def eight():
    a()
    b()
    c()
    d()
    e()
    f()
    g()

def nine():
    a()
    b()
    c()
    d()
    en()
    f()
    g()

def zero():
    a()
    b()
    c()
    d()
    e()
    f()
    gn()


def nothing():
    an()
    bn()
    cn()
    dn()
    en()
    fn()
    gn()


def display0():
    GPIO.output(Display0, GPIO.LOW)
    GPIO.output(Display1, GPIO.HIGH)
    GPIO.output(Display2, GPIO.HIGH)
    GPIO.output(Display3, GPIO.HIGH)

def display1():
    GPIO.output(Display0, GPIO.HIGH)
    GPIO.output(Display1, GPIO.LOW)
    GPIO.output(Display2, GPIO.HIGH)
    GPIO.output(Display3, GPIO.HIGH)

def display2():
    GPIO.output(Display0, GPIO.HIGH)
    GPIO.output(Display1, GPIO.HIGH)
    GPIO.output(Display2, GPIO.LOW)
    GPIO.output(Display3, GPIO.HIGH)

def display3():
    GPIO.output(Display0, GPIO.HIGH)
    GPIO.output(Display1, GPIO.HIGH)
    GPIO.output(Display2, GPIO.HIGH)
    GPIO.output(Display3, GPIO.LOW)


def print_to_seg7(distance):


    distance = round(distance, 0)

    print(distance)

    tausender = (distance - (distance % 1000)) / 1000

    hunderter = (distance - (distance - (distance % 1000)) - distance % 100) / 100

    zehner = ((distance - (distance - (distance % 1000)) - distance % 10) - (
            distance - (distance - (distance % 1000)) - distance % 100)) / 10

    einer = (distance - (distance - (distance % 1000))) - zehner * 10 - hunderter * 100

    for x in range (4):
        wert[x]

    wert[0] = einer

    wert[1] = zehner

    wert[2] = hunderter

    wert[3] = tausender




numbers = {
            0 : zero,
            1 : one,
            2 : two,
            3 : three,
            4 : four,
            5 : five,
            6 : six,
            7 : seven,
            8 : eight,
            9 : nine,
        }

display = {
            0 : display0,
            1 : display1,
            2 : display2,
            3 : display3,
}




wert = [0,0,2,1]

ca = 0

h = 0



if __name__ == '__main__':
    try:
        reset()
        while True:
            if (h >= 100):
                value = ultraschallsensor()
                print_to_seg7(value)
                h = 0

            h = h + 1

            for x in range(4):
                nothing()
                display[x]()
                ca = wert[x]
                numbers[ca]()
                time.sleep(0.001)

            if(ultraschallsensor()> 30):
                goforward()
            if(ultraschallsensor()<30):
                stop()





        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("")
        GPIO.cleanup()