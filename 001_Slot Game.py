# Slot Game

import random

MAX_LINES = 3
MIN_BET = 100
MAX_BET = 1000
ROWS = 3
COLM = 3
SYMBOLS = {"🎇":2,"🎈":3,"💎":4,"🎶":5}
SYMBOLS_VALUE = {"🎇":3,"🎈":2.5,"💎":2,"🎶":1.5}

def check_winnings(columns,lines,bet,values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol]*bet
            winning_lines.append(line + 1)
    return winning,winning_lines

def get_slot_machine_spin(rows,colm,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns=[]
    for _ in range(colm):
        row=[]
        copy_symbols=all_symbols[:]
        for _ in range(rows):
            value = random.choice(copy_symbols)
            copy_symbols.remove(value)
            row.append(value)

        columns.append(row)
    return columns 

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()

def deposit():
    while True:
        amount = input("Enter the amount you want to Deposit\n------> ₹ ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 100:
                break
            else:
                print("You need to Deposit at least ₹100.\n ")
        else:
            print("Don't joke around!\nJust enter a whole number.\n ")
    return amount

def num_of_lines():
    while True:
        lines=input("Enter the number of lines you want to Bet on (1-"+str(MAX_LINES)+")\n------> ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("You need to choose between 1-"+str(MAX_LINES)+"\n ")
        else:
            print("Don't joke around! Just enter a whole number.\n ")
    return lines

def get_bet():
    while True:
        amount=input("Enter the amount you want to Bet on each line\n------> ₹ ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"You need to Bet between ₹{MIN_BET} - ₹{MAX_BET}.")
        else:
            print("Don't joke around!\nJust enter a whole number.\n ")
    return amount

def spin(balance):
    lines = num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"You don't have enough balance to bet ₹{bet} on {lines} lines.\nYour Current total balance is ₹{balance}\n")
        else:
            break
    print(f"You are betting ₹{bet} on {lines} lines.\nYour total bet is of ₹{total_bet}")

    slots = get_slot_machine_spin(ROWS,COLM,SYMBOLS)
    print_slot_machine(slots)
    winning,winning_lines = check_winnings(slots,lines,bet,SYMBOLS_VALUE)
    print(f"You Won on Lines : ",*winning_lines)
    print(f"You Won ₹{winning}.")
    return winning - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ₹{balance}.")
        answer = input("Press Enter to spin (q to quit) : ")
        if answer == 'q':
            break  
        # if balance == 0:
        #     deposit()
        balance += spin(balance)
    print(f"You left with ₹{balance}")

main()

