import threading
import time
import os

zvezdice1 = []
zvezdice2 = []
zvezdice3 = []
zvezdice4 = []

for i in range(40):
    zvezdice1.append(" ")
    zvezdice2.append(" ")
    zvezdice3.append(" ")
    zvezdice4.append(" ")

def zvezdice_lista():
    global zvezdice1, zvezdice2, zvezdice3, zvezdice4
    for i in range(40):
        zvezdice1[i]= " "
        zvezdice2[i]= " "
        zvezdice3[i]= " "
        zvezdice4[i]= " "

def brojevi (number, n):
    num = number

    if(n == 1):
        num += 1
    elif(n == 2):
        num -= 1

    return num

def time_print(sec):

    zvezdice_lista()

    while True:
        z = 0
        a = 0
        for i in range(40):
            if(z == 0):
                zvezdice1[i] = "*"
            if(z == 1):
                zvezdice2[i] = "*"
            if(z == 2):
                zvezdice3[i] = "*"
            if (z == 3):
                zvezdice4[i] = "*"

            print(''.join(zvezdice1))
            print(''.join(zvezdice2))
            print(''.join(zvezdice3))
            print(''.join(zvezdice4))
            time.sleep(sec)
            os.system("cls")

            zvezdice_lista()

            a += 1

            if(a < 4):
                z = brojevi(z, 1)
            elif(a == 7):
                z = brojevi(z, 1)
                a = 1
            elif(a > 3):
                z = brojevi(z,2)

t1 = threading.Thread(target=time_print, args=(1,))
t1.start()
