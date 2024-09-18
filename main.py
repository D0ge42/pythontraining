import math

# radius = float(input("ENter the radius of a circle: "))
#
# circ = 2 * math.pi * radius
# area = math.pi * pow(radius,2)
#
# print(f"The circumference is {round(circ,2)} cm")
# print(f"The area of the circle is {round(area,1)}cm²")
# #
# ----------------------------------------------------------
# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
#
# c = math.sqrt(pow(a, 2) + pow(b, 2))
#
# print(f"Side C is = {c}")
#
# ----------------------------------------------------------
#
# age = int(input("Enter your age: "))
#
# if age >= 100:
#     print("You're too old!")
# elif age >= 18:
#     print("You're now signed up!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You must be 18+ to sign up")
# -------------------------------------------------------------
# response = input("Would you like some food? (Y/N): ")
#
# if response == "Y":
#     print("Magna")
# else:
#     print("Nun magna")
# # ---------------------------------------------------------------
# name = input("Enter your name: ")
# if name == "":
#     print("Please enter a name")
# else:
#     print(f"Hello {name}")
# # ------------------------------------------------------------------
#
# number = (float(input("Enter a number: ")))
# sign = input("Enter a sign: ")
# number2 = (float(input("Enter a second number ")))
#
# if sign == "+":
#     print(f"Result is equal to {number + number2}")
# elif sign == "/":
#     print(f"Result is equal to {number / number2}")
# elif sign == "*":
#     print(f"Result is equal to {number * number2}")
# elif sign == "-":
#     print(f"Result is equal to {number - number2}")
# else:
#     print(f"{sign} is not valid")
# ---------------------------------------------------------------------
#
# weight = float(input("Enter your weight: "))
# unit = input("What's your unit system, Kilograms or Pounds (K or P): ")
#
# if unit == "P":
#     weight = weight * 2.205
#     unit = "pounds"
# elif unit == "K":
#     unit = "Kgs"
# else:
#     print("Invalid unit provided")
# print(f"Your weight in {unit} is {weight} {unit}")
#
# -------------------------------------------------------------------------
#
# unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
# temp = float(input("Enter temperature: "))
#
# if unit == "C":
#     temp = round(((9 * temp) / 5 + 32),1)
#     print(f"Temperature in Fahrenheit is: {temp}°F")
# elif unit == "F":
#     temp = round(((temp - 32) * 5 / 9),1)
#     print(f"Temperature in Celsius is: {temp}°C")
# else:
#     print(f"{unit} is not valid")
# ----------------------------------------------------------------------------
# num = -5
#
# print("Positive" if num > 0 else "Negative")
#
# -----------------------------------------------------------------------------
#
# name = input("Enter your full name: ")
# result = len(name)
# result = name.find("o")
# result = name.rfind("o")
# name = name.capitalize()
# name = name.upper()
# result = name.count("o")
# name = name.replace("o", "u")
# print(name)

# # --------------------------------------------------------------------------------
#
# name = input("Enter your name: ")
# if len(name) > 12:
#     print("Name is too long!")
# elif not name.find(" ") == -1:
#     print("Name can't contain spaces")
# elif not name.isalpha():
#     print("Name can't contain digits")
# else:
#     print(f"Your name is {name}")
# ----------------------------------------------------------------------------------
# #[start: end: step] --> indexing operators.
# credit_number = "1233-3123-3123-1233"
#
# print(credit_number[0:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::2])
# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")
# reverse_number = credit_number[::-1]
# print(f"{reverse_number}")
# -----------------------------------------------------------------------------------
# #
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
#
# print(f"price 1 is {price1:10}")
# print(f"price 1 is {price2:^10}")
# print(f"price 1 is {price3:>10}")
#
# -------------------------------------------------------------------------------------
#
# name = input("Enter your name: ")
# while name=="":
#     name = input("Enter your name: ")
# else:
#     print(f"Hello {name}")
# --------------------------------------------------------------------------------------
#
# age = int(input("Enter your age: "))
# while age < 18:
#     print("You're not 18 yet!")
#     age = int(input("Enter age: "))
# print(f"You're now {age}")
# ---------------------------------------------------------------------------------------
#
# principle = 0
# rate = 0
# time = 0
#
# while True:
#     principle = float(input("Enter principle amount: "))
#     if(principle < 0):
#         print("principle can't be equal to or less than 0")
#     else:
#         break
# while True:
#     rate= float(input("Enter interest rate: "))
#     if(rate < 0):
#         print("Interest rate can't be equal to or less than 0")
#     else:
#         break
# while True:
#     time = int(input("Enter the time in years: "))
#     if time < 0:
#         print("Time can't be 0 or negative")
#     else:
#         break
# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time} year/s: ${total:.2f}")
#
# --------------------------------------------------------------------------------------
#

# for x in reversed(range(0,11)):
#     print(x)
# print("Happy new YEAR!")
# name = "lorenzo"
# for x in name:
#     if x == "e":
#         continue
#     else:
#         print(x)
# --------------------------------------------------------------------------------------
# import time
#
# my_time = int(input("Enter time in seconds: "))
#
# for x in range (my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
#
# print("time's up!")
#
# -----------------------------------------------------------------------------------------
# rows = int(input("Enter number of rows: "))
# columns = int(input("ENter the # of columns: "))
# symbol = input("Enter a symbol to use: ")
#
# for y in range(rows):
#     for x in range(columns):
#          print(symbol, end="*")
#     print()
# -------------------------------------------------------------------------------------------

# fruits = {"apple", "orange", "banana", "coconut"}
# #
#
# # #
# # # fruits.append("pineapple")
# # # print(fruits)
# # # fruits.remove("apple")
# # # print(fruits)
# # # fruits.insert(0,"pineapple")
# # # print(fruits)
# # print(dir(fruits))
#
# ----------------------------------------------------------------------------------------
#
# foods = []
# prices = []
# total = 0
#
# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $ "))
#         foods.append(food)
#         prices.append(price)
# list_len = len(foods)
# count = 0
# print("-----YOUR SHOPPING CART------")
# for food in foods:
#     print(f"Article n°{count} is {food}, price is ${prices[count]}")
#     count+=1
# print()
# print("------TOTAL-----")
# for price in prices:
#     total += price
# print(f"Your total is ${total:^} ")
# ---------------------------------------------------------------------------------
# fruits = ["banana", "orange", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats =["chicken", "fish","turkey"]
#
# groceries = [fruits, vegetables, meats]
# print(groceries)
# -----------------------------------------------------------------------------------
# num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()
# -------------------------------------------------------------------------------------
# RED = "\033[91m"
# GREEN = "\033[92m"
# CYAN = "\033[96m"
# YELLOW = "\033[93m"
# MAGENTA = "\033[95m"
# RESET = "\033[0m"  # Resets the color to default
# questions = (("Quanti giri fa una boccia"),
#              ("Se ocane ha un cane, di chi è il cane"),
#              ("Apelle figlio di apollo fece una palla di pelle di..."),
#              ("La smantequila de la.."),
#              ("Sono talmente sgravato che mi chiamavano..."))
# options = (("A. 12", "B. 112", "C. Finchè non si ferma","D. Ma io che cazzo ne so scusi", "E. la cipolla"),
#            ("A. Del signor ocane", "B. Mio, sono il signor ocane", "C. Dell'immenso","D. Ma io che cazzo ne so scusi", "E. 42"),
#            ("A. cashemere", "B. di pelle", "C. Sì","D. Ma io che cazzo ne so scusi", "E.eeeee macarena"),
#            ("A. muerte", "B. soy un chico muy loco", "C. FOzza roma","D. Ma io che cazzo ne so scusi", "E. benvenutiragazzieragazzeinquestonuvovideo"),
#            ("A. l'imbarazzante","B. Slork","C. la muerte","D. Kevin methnick","E. Omobofo"))
# answers = (("D"),("C"),("C"),("A"),("B"))
# possible_answers = (("A"),("B"),("C"),("D"),("E"))
# question_num = 0
# x  = 0
# y = 0
# score = 0
# # import pdb
# # pdb.set_trace()
# print(f"{MAGENTA} Benvenuto nel python quiz game! {RESET}")
# for question in questions:
#     print(f"{YELLOW}Domanda n° {question_num}. {questions[question_num]}{RESET}"udo
#     print()
#     for option in options:
#         print(f"{options[x][y]}")
#         y+=1
#     print()
#     user_guess = input("Enter a letter (A-E): ").upper()
#
#     if(user_guess == answers[question_num]):
#         print()
#         print(f"{GREEN}-----You guessed right-----{RESET}")
#         score +=1
#     else:
#         print(f"{RED}----Wrong, right answer was {answers[question_num]}-----{RESET}")
#     y = 0
#     x += 1
#     question_num+=1
#     print()
# print(f"{GREEN}----------FINALE SCORE----------{RESET}")
# print(f"Your finale score is {score:}")
# ---------------------------------------------------------------------------------------------------------

# capitals = {"USA":"Washington D.C.", "India": "New Delhi", "China":"Beijing","Italy":"Rome"}
#
# print(capitals.get("USA"))
#
# if(capitals.get("India")):
#     print("Capital exists")
# else:
#     print("Capital doesn't exists")
#
# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA": "Detroit"})
#
# for key in capitals.keys():
#     print(key)
# for value in capitals.values():
#     print(value)
# for key, value in capitals.items():
#     print(f"{key}:{value}")
# -------------------------------------------------------------------------------------------------------------
#
# menu = {"pizza": 3.00, "popcorn":2.00, "fries":3.00, "soda":3.00}
#
# cart = []
# total = 0
# print("------MENU------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("-------------------")
#
# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")
# print()
# print("-----TOTAL---------")
# print(f"Total is: ${total:.2f}")
# ----------------------------------------------------------------------------------------------------------------
# import random
# options = ["rock", "paper", "scissors", "carta", "forbice"]
# #print(random.choice(options))
# random.shuffle(options)
# print(options)
# ------------------------------------------------------------------------------------------------------------------
#
# import random
# options = ("rock", "paper", "scissors")
#
# player = None
# answer = None
# computer = random.choice(options)
#
# while True:
#     if(answer == "n"):
#         break
#     else:
#         computer = random.choice(options)
#         print("-------------ROCK PAPER SCISSORS GAME!-----------------")
#         player = input("Choose between rock, paper and scissors: ")
#         while player not in options:
#             player = input("Choose a valid input: ")
#             if(player in options):
#                 break
#         if((player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player =="paper" and computer == "rock")):
#             print(f"Computer choosed {computer}, You won!")
#             print("---------------------------------------")
#         elif(player == computer):
#             print(f"Draw!, you  choosed {player} and computer choosed {computer} ")
#             print("---------------------------------------")
#         else:
#             print(f"You lost! Computer choice was {computer} and your was {player}")
#             print("---------------------------------------")
#         answer = input("Do you wanna keep playing? (Y/N): ").lower()
#         print()
# ------------------------------------------------------------------------------------------------------------------------
#
# def add_sum(num1, num2):
#     return num1 + num2
#
# print(add_sum(4,9))
# --------------------------------------------------------------------------------------------------------------------------
# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)
#
# print(net_price(300, 0.1))
# ---------------------------------------------------------------------------------------------------------------------------
# import time
#
# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")
#
# count(10)
# # -----------------------------------------------------------------------------------------------------------------------------
#
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(18,1,2,31,312,3,123,12,321))
# ------------------------------------------------------------------------------------------------------------------------------
# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)
#
# print_address(street = "123 fake st.", city= "Derni", state="dindorni")
# ---------------------------------------------------------------------------------------------------------------------------------
# numbers = [1,2,3,4,5]
#
# for item in numbers:
#     print(item)
# ------------------------------------------------------------------------------------------------------------------------------------
# word = "derni"
#
# letter = input("Guess a letter in the secret word: ").lower()
#
# if(letter in word):
#     print(f"Yes, {letter} is present in the given word")
# else:
#     print(f"Sorry, {letter} is not present in the given word")
# ----------------------------------------------------------------------------------------------------------------------------------------
# grades = {"Doge":2, "Cavi":3, "Buddy":4, "Musturu":5}
#
# student = input("Enter the name of a student: ")
#
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")
# -----------------------------------------------------------------------------------------------------------------------------------------

# email = input("Enter your email address: ")
#
# if "@" in email and "." in email:
#     print("Email is valid")
# elif "@" in email and "." not in email:
#     print("Email is not valid. '.' is missing")
# elif "@" not in email and "." in email:
#     print("Email not valid. '@' is missing")
# else:
#     print("Email not valid.")
# --------------------------------------------------------------------------------------------------------------------------------------------
# doubles = [x * 2for x in range(1, 11)]
# squares = [x * x for x in range (1, 11)]
# fruits = ["orange", "apple", "banana", "coconut"]
# fruits_chars = [fruit[0] for fruit in fruits ]
# print(doubles)
# print(squares)
# print(fruits_chars)
# numbers = [1, -2, 3, -4, 5, -6, 8]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num %2 == 0]
# print(positive_nums)
# print(negative_nums)
# print(even_nums)
#
# grades = [85, 42, 79, 90, 56, 61, 30]
#
# passing_grades = [grade for grade in grades if grade >= 60]
#
# print(passing_grades)
#---------------------------------------------------------------------------------------------------------------------------------------------------
# def day_of_week(day):
#     match day:
#         case "lunedì":
#             return True
#         case 2:
#             return "martedì"
#         case _:
#             return "not a valid day"
# print(day_of_week("lunedì"))
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# import math as m
#
# print(m.pi)
# -----------------------------------------------------------------------------------------------------------------------------------------------------

# balance = 0
# is_running = True
# option_list = ["1.Show Balance", "2.Deposit", "3.Withdraw", "4.EXIT"]
# option_next_list = ["1.Yes", "2.Exit"]
# def show_balance():
#     print(f"Your balance is ${balance:.2f}💰")
#
#
# def deposit():
#     money = float(input(f"How many money would you like to deposit? "))
#     return money
#
# def withdraw():
#     money_withdraw = float(input(f"How many money would you like to withdraw? "))
#     return money_withdraw
#
# while is_running:
#     print("----BANKING PROGRAM-----")
#     print("---CHOOSE AN OPTION---")
#     for option in option_list:
#         print(f"{option}")
#     choice = input("Enter your choice (1-4): ")
#     match choice:
#         case "1":
#             show_balance()
#         case "2":
#             amount = deposit()
#             if(not amount):
#                 print("You cannot deposit 0 or less $")
#             else:
#                 balance += amount
#                 print("Your bank balance has been updated 💸 ")
#         case "3":
#             amount = withdraw()
#             if balance - amount >= 0:
#                 balance -= amount
#                 print("Your bank balance has been updated")
#             else:
#                 print(f"You do not have that many money. Your current balance is ${balance:.2f}")
#         case "4":
#             break
#     next = input("Do you want to do something else? (Yes/no) ").lower()
#     match next:
#         case "yes"| "y":
#             continue
#         case "no" | "n":
#             break
# print("------THANKS AND GOODBYE :)------")
# ----------------------------------------------------------------------------------------------------------------
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
        print(f"{YELLOW}---{items}---{RESET}", end=" ")

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
