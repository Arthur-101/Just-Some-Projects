import time
import random
from playsound import playsound as ganna

a=8
line=200
s=''
emoji=['🌟','⭐','❄','🎈','🎵','✨']
for _ in range(1,35):
    print('')
for line_s in range(1,120):
    if line in [200,160,120,80,40,0]:
        ganna('Items\\new year.mp3',block=False)
    column=random.randint(1,119)
    while (column > 0):
        s += ' '
        column -= 1    
    if (line_s % 10==0):
        print(s+"HAPPY NEW YEAR 2023")
    else:
        print(s+random.choice(emoji))
    s=''
    time.sleep(0.2)
    line -= 1
print("       🌟\n       *\n      * *\n     * * *\n HAPPY NEW YEAR    ")
for _ in range(5,a):
    for __ in range(a-_):
        print(" ",end='')
    for __ in range(_):
        print('* ',end='')
        time.sleep(0.05)
    print()
for _ in range(int(a/2),a):
    for __ in range(a-_):
        print(" ",end='')
    for __ in range(_):
        print('* ',end='')
        time.sleep(0.05)
    print()
for __ in range(int(a/2),a):
    for _ in range(a-__):
        print(" ",end='')
    for _ in range(__):
        print('* ',end='')
        time.sleep(0.05)
    print()
for _ in range(int(a/2)):
    print("      *",end='')
    for __ in range(int(a/4)):
        print('*',end='')
        time.sleep(0.1)
    print()
print(".......... May This Year Brings You Happiness And Many Opportunities At The Same Time .........\n")
print(" "*80+"-- ARTHUR\n\n")
