import random
import time
from os import system

def wait(x):
    for i in range(x):
        time.sleep(1)
        print("Czas który upłynoł: ", i+1)
    system('cls')

def generate (t,n):
    a = 0
    b = 0
    c = 0
    for i in range(n):
        print(a, b, c)
        wait(t)
        a = random.randint(0,10)
        b = random.randint(0,10)
        c = random.randint(0,10)
    print(a, b, c)

generate(1,5)