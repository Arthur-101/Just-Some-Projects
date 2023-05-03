import pyfiglet
import time
from termcolor import colored,cprint
import colorama
# from colorama import Fore,Back,Style
colorama.init()

wish=['GOOD','MORNING ,','INDIA .','WORLD ,','UNIVERSE']
count=0
# colors=[Fore.RED,Fore.WHITE,Fore.GREEN,Fore.CYAN,Fore.BLUE]
colors2=['red','white','green','red','blue']

def space(n):
    for _ in range(n):
        print("")
    time.sleep(0.5)

def write(text,tsleep):
    space(35)
    print(" "*50+text)
    space(15)
    time.sleep(tsleep)

# write("HEY BUDDY!!",2)
# space(35)
# cprint(pyfiglet.figlet_format("HELLO!!",font='starwars',width=150),'yellow')

for i in range(len(wish)+1):
    if count>4:
        cprint('*'* 60,'white')
        count=0
    else:
        color=colors2[count]
        msg=pyfiglet.figlet_format(wish[count],font='starwars',width=150)
        # cprint(color+msg)
        cprint(msg,color)
        count=count+1
        time.sleep(0.5)

