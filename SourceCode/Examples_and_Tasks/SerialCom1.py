import serial
import time

ard = serial.Serial('com3',9600);

while True:
    a=70
    b=53
    s=str(a)+";"+str(b)+"."
    ard.write(s.encode())
    time.sleep(0.1)
    ar=ard.readline()
    print(ar)
