import socket
import random
import time


def losowanie():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    kord = [a, b, c]
    return kord


def client(n, t):
    host = socket.gethostname()
    port = 8080

    s = socket.socket()
    s.connect((host, port))

    czas = t
    s.send(str(czas).encode('utf-8'))
    for i in range(n):
        message = losowanie()
        kord = ""
        for h in message:
            kord += str(h) + " "
        print(kord)
        s.send(kord.encode('utf-8'))
        time.sleep(t)
    message = 'stop'
    s.send(message.encode('utf-8'))


print("Wprowadz n: ")
n = input()
while int(n) < 5:
    print("Za maly n. Wprowadz jeszcze raz: ")
    n = input()
print("Wprowadz t: ")
t = input()
client(int(n), int(t))
