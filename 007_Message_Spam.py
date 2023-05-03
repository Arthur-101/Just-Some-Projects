import pyautogui as spam
import string
import random
import time as t

what0 = input("1. Auto Spam\n2. Custom Spam\n-----> ")
what = what0.upper()
num = input("Enter number of Messages you want to send\n-----> ")
if what=='A' or what=='AUTO' or what=='1':
    len=input("Enter the length of Spam (in letters)\n-----> ")
    t.sleep(5)
    for i in range(int(num)):
        auto=''.join(random.choices(string.digits+string.ascii_letters,k=int(len)))
        spam.typewrite(auto)
        spam.press('Enter')
        t.sleep(0.3)
elif what=='C' or what=='CUSTOM' or what=='2':
    msg = input("Enter the Message you want to send\n-----> ")
    t.sleep(5)
    for _ in range(int(num)):
        spam.typewrite(msg)
        spam.press('Enter')
        t.sleep(0.3)
else:
    print("INVALID INPUT!!!\nTRY AGAIN.....")
