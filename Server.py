# Echo server program
import socket
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

data = 'e'

if __name__ == '__main__':
    try:
        HOST = ''  # Symbolic name meaning all available interfaces
        PORT = 50007  # Arbitrary non-privileged port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        print('Connected by', addr)

        while True:

            input_left = GPIO.input(18)
            input_right = GPIO.input(15)
            input_forward = GPIO.input(14)
            input_backwards = GPIO.input(16)
            input_stop =  GPIO.input(20)

            alr = 0
            if input_forward == False and alr == 0:
                time.sleep(0.2)
                data = 'w'
                conn.sendall(data)
                alr = 1

            if input_left == False and alr == 0:
                time.sleep(0.2)
                data = 'a'
                conn.sendall(data)
                alr = 1

            if input_right == False and alr == 0:
                time.sleep(0.2)
                data = 'd'
                conn.sendall(data)
                alr = 1
            if input_backwards == False and alr == 0:
                time.sleep(0.2)
                data = 's'
                conn.sendall(data)
                alr = 1
            if input_stop == False and alr == 0:
                time.sleep(0.2)
                data = 'p'
                conn.sendall(data)
                alr = 1





    except KeyboardInterrupt:
        print("")
        GPIO.cleanup()
        conn.close()
