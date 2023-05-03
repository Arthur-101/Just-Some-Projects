import random
import time

a01 = ['0','1']
# space = random.randint(10,40)
timer = [0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25]

def k():
    return random.choice(a01)

for i in range(300):
    time.sleep(random.choice(timer))

    for j in range(40):
        space = random.randint(1,40)
        print(' '*space,k(),end=' ')
    
    print()
