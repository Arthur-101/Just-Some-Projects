import pyautogui as spam
import time
import random

num = input("Enter number of Messages you want to send\n-----> ")
a=["Monkey","Donkey","Cat","Dog","Rat","Snake"]
time.sleep(6)
for _ in range(int(num)):
    ran=random.choice(a)
    spam.typewrite("You are a "+ran)
    spam.press('Enter')
    time.sleep(0.5)
