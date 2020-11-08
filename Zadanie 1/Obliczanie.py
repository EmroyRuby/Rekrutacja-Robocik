import socket
import math

host = socket.gethostname()
port = 8080

s = socket.socket()
s.bind((host, port))
s.listen()
conn, addr = s.accept()

cord_pop = [0, 0, 0]
with conn:
    print('Connected by ', addr)
    czas = float(conn.recv(1024).decode('utf-8'))
    while True:
        cord = conn.recv(1024).decode('utf-8')
        if not cord:
            break
        if cord == "stop":
            s.close()
            print("Zakonczono pracę")
            break
        cord = cord.strip().split()
        print(cord)
        droga = 0
        for i in range(3):
            a = math.fabs(int(cord_pop[i]) - int(cord[i]))
            droga += a * a
        predkosc = droga/czas
        print("predkosc:", predkosc)
        cord_pop = cord
