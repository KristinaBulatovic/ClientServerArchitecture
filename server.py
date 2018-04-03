import socket
import threading
import time
import os

def time_print(sec):
    zvezdice = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    while True:
        time.sleep(sec)
        for i in range(1,10):
            zvezdice[i] = "*"
            print(''.join(zvezdice))
            time.sleep(sec)
            os.system("cls")
            zvezdice = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

t1 = threading.Thread(target=time_print, args=(2,))

s = socket.socket()
host = 'localhost'
port = 12346

s.bind((host,port))
s.listen(5)

num = 0

t1.start()
while True:
    conn, addr = s.accept()
    num += int(conn.recv(1024).decode())
    conn.send(str(num).encode())
    conn.close()