import random
import time

# Color definitions using ANSI escape codes
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Reset color
RESET = "\033[0m"

balance = 100
cost = 10
emojis = ["🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩","🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩",
          "🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩","🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩",
          "🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩","🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩",
          "🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩","🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩",
          "🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩","🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩",
          "🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩","🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩",
          "🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩","🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩",
          "🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩","🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩",
          "🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩","🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩",
          "🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩","🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩",
          "🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩","🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩",
          "🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩","🍎","🥭","🍑","🍓","🥝","🌶️","🍆","🌽","🥩"]
list = [f"{BLUE}1.Play", f"2.Show Balance", "3.Withdraw.",f"4.Exit{RESET}"]


def spin_row():
    random.shuffle(emojis)
    first_row = [emojis[0],emojis[1],emojis[2]]
    second_row = [emojis[3],emojis[4],emojis[5]]
    third_row = [emojis[6],emojis[7],emojis[8]]
    complete = [first_row,
                second_row,
                third_row]
    return complete

def show_balance():
    return balance

def withdraw():
    money = float(input("How many money would you like to withdraw? "))
    return money

def check_match(board):
    if ((board[0][0] == board[0][1] and board[0][0] == board[0][2]) or 
        (board[1][0] == board[1][1] and board[1][0] == board[1][2]) or 
        (board[2][0] == board[2][1] and board[2][0] == board[2][2])):
        return True
    else:
        return False

def print_comb(comb):
    for items in comb:
        print(f"{YELLOW} | {items} | {RESET}", end=" ")

def deposit(amount):
    return amount



while True:

    if balance < 10:
        print("You don't have enough money to gamble!")
        choice = input("Do you want to deposit more money? (Y/N): ").lower()
        match choice:
            case "y":
                money = float(input("How many dollars?: "))
                balance += deposit(money)
                print(f"{BRIGHT_BLUE}You've successfully deposited ${money:.2f}. Your balance is now ${balance:.2f}{RESET}")
            case "n":
                break
    else:
        print(f"{MAGENTA}---WELCOME TO LAS DOGES---{RESET}")
        print(f"{YELLOW}CURRENT BALANCE ${balance:.2f}{RESET}")
        print(f"--{CYAN}CHOOSE AN OPTION{RESET}--")
        for item in list:
            print(item)
        choose = input("Enter your choice: ")
        match choose:
            case "1":
                balance -= cost
                print("Spinning...")
                for x in range(1,2):
                    time.sleep(1)
                complete = spin_row()
                list1 = complete[0]
                list2 = complete[1]
                list3 = complete[2]
                print_comb(list1)
                print()
                print_comb(list2)
                print()
                print_comb(list3)
                print()
                amount = random.randint(0,100)
                if check_match(complete) == 1:
                    print(f"{GREEN}CONGRATZ!!! You won ${amount}{RESET}")
                    balance += amount
                    print("-------------------")
                    print(f"Your balance is ${balance}")
            case "2":
                print(f"{MAGENTA}*******************************{RESET}")
                print(f"    YOUR BALANCE IS {BRIGHT_GREEN}${balance:.2f}{RESET}     ")
                print(f"{MAGENTA}*******************************{RESET}")
            case "3":
                money = withdraw()
                balance -= money
                print(f"{BRIGHT_BLUE}You've successfully withdrawn ${money:.2f} and your balance is {balance:.2f}{RESET}")
            case "4":
                break

