import random
import time

def k():
    return random.choice([0,1])

for i in range(100):
    t = random.choice([0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25])
    time.sleep(t)
    for j in range(70):
        print(k(),end=' ')

    print("")
