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

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $ "))
        foods.append(food)
        prices.append(price)
list_len = len(foods)
count = 0
print("-----YOUR SHOPPING CART------")
for food in foods:
    print(f"Article n°{count} is {food}, price is ${prices[count]}")
    count+=1
print()
print("------TOTAL-----")
for price in prices:
    total += price
print(f"Your total is ${total:^} ")
