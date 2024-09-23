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
#------------------------------------------------------------------------------------------------------------------------------------
# import random
# import string
#
# chars = string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()
# random.shuffle(key)
#
# user_input = input("Enter a phrase to encrypt: ")
# cipher_text = ""
#
# for letter in user_input:
#     index = chars.index(letter)
#     cipher_text += key[index]
#
# print(f"encrypted message: {cipher_text}")
# decrypted_text =""
# choice = input(f"Do you wanna decrypt this message {cipher_text}(Yes/no)?: ").lower()
# match choice:
#     case "yes" | "y":
#         for letter in cipher_text:
#             index = key.index(letter)
#             decrypted_text += chars[index]
#         print(f"Decrypted message: {decrypted_text}")
#     case "no" | "n":
#         print("Goodbye!")
#------------------------------------------------------------------------------------------------------------------------------------------
# from car import Car
#
# car1 = Car("Ferrari", "2024","Red",False)
# car2 = Car("Tesla","2025","blue",False)
#
# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car1.for_sale)
# car1.drive()
# class Student:
#
#     class_year = 2024
#     num_students = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students+=1
#
# student1 = Student("Spongebob", 30)
# student2 = Student("Patrick", 35)
# student2 = Student("Mr.Plancton", 35)
# student2 = Student("Erpup1", 35)
# student2 = Student("Patrick", 35)
#
# print(student1.name)
# print(student2.age)
# print(student1.class_year)
# print(student2.class_year)
# print(Student.class_year) #Usually accessed by class Name
# print(Student.num_students)
# -----------------------------------------------------------------------------------------------------------------------------------------
# class Animal:
#     def __init__(self, name):
#         self.name=name
#         self.is_alive = True
#
#     def eat(self):
#         print(f"{self.name} is eating")
#
#     def sleep(self):
#         print(f"{self.name} is sleeping")
#
# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")
# class Cat(Animal):
#           pass
# class Mouse(Animal):
#         pass
#
# dog = Dog("Sheela")
# cat = Cat("Zuya")
# mouse = Mouse("Topenzo")
#
# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()
# dog.speak()
# -----------------------------------------------------------------------------------------------------------------------------------------
# class Animal:
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f"{self.name} is eating")
#
# class Prey(Animal):
#     def flee(self):
#         print(f"This {self.name} is fleeing")
#
# class Predator(Animal):
#     def hunt(self):
#         print(f"This animal is hunting")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator):
#     pass  
#
# rabbit = Rabbit("Bugs")
#
# hawk = Hawk("Tony")
#
# fish = Fish("Nemo")
#
# rabbit.eat()
# --------------------------------------------------------------------------------

#super() = Function used in a child class to call methods from a parent class(superclass)
# Allows you to extend the functionality of the inherited methods
# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled
#
#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
#
# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius
#
#     def describe(self):
#         print(f"The circle as an area of {3.14 * self.radius * self.radius}cm^2")
#         super().describe()
#
# class Square(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.width = width
#
# class Triangle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.height = height
#         self.width = width
#
# circle = Circle("red",True, radius=5)
# print(circle.describe())
# print(circle.color)
# print(circle.is_filled)
# print(f"{circle.radius}cm")

# class Furniture:
#     def __init__(self,name,color, material, width, height):
#         self.name = name
#         self.color = color
#         self.material = material
#         self.width = width
#         self.height = height
#
#     def describe(self):
#         print(f"Furniture name is: {self.name}")
#
# class Window(Furniture):
#     def __init__(self,name,color, material, width, height):
#         super().__init__(name,color, material, width, height)
#
#     def describe(self):
#         super().describe()
#         print(f"{self.color} and made out of {self.material}. It is {self.width}cm large and its height is {self.height}")
#
# window = Window("window","red","wood and glass","40cm","80cm")
# print(window.color)
# print(window.describe())
#

# --------------------------------------------------------------------------------------

# from abc import ABC, abstractmethod
#
# class Shape:
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return (self.base * self.height)/2
#
# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping = topping
#
#
# shapes = [Circle(4),Square(5),Triangle(6,7), Pizza("Margherita", 5)]
#
# for shape in shapes:
#     print(f" {shape.area()}")
# ------------------------------------------------------------------------------
#"Duck tipying" = Another way to achieve polymophism besides inheritance.
# Object must have the minimum necessary attributes/methods.
#"If it looks like a duck and quacks like a duck, it must be a duck"

# class Animal:
#     alive = True
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof!")
#
# class Cat(Animal):
#     def speak(self):
#         print("Miao")
#
# class Car:
#
#     alive = False
#     def speak(self):
#         print("Honk!")
#
# animals = [Dog(), Cat(), Car()]
#
# for animal in animals:
#     animal.speak()
#     print(animal.alive)

# --------------------------------------------------------------------------------

#static methods = best for utility functions that do not need access to class data.
#Instance methods = Best for operations on instances of the class (objects)

# class Employee:
#
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     def get_info(self):
#         return f"{self.name} = {self.position}"
#
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
#         return position in valid_positions
#
#
#
# employee1 = Employee("Eugene", "Manager")
# employee2 = Employee("Squidward", "Cashier")
# employee3 = Employee("Spongebob", "Cook")
#
# print(Employee.is_valid_position("Cook"))
#
# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())

# --------------------------------------------------------------------------------
#CLass methods = Allow operations related to the class itself.
                 #Takes (cls) as first parameter, which represents the class itself
#Instance method = Best for operations on instances of the class(objects)
# Static methods = Best for utility functions that do not need access to class data
# #class methods = Best for class-levels data or require access to class itself.
# class Student:
#
#     count = 0
#     total_gpa = 0
#
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa
#
#         #Instance method
#     def get_info(self):
#             return f"{self.name} {self.gpa}"
#
#     @classmethod
#     def get_count(cls):
#             return f"Total # of students: {cls.count}"
#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
#
#
# student1 = Student("Spongebob", 3.2)
# student2 = Student("Patrick", 2.0)
# student3 = Student("Sandy", 4.0)
# print(Student.get_count())
# print(Student.get_average_gpa())
# print(student1.get_info())
#
# ---------------------------------------------------------------------------------
#Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#Authomatically called by many of python's built in operations.
#They allow developers to define or customize the behavior of objects

# class Book:
#
#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages
#
#     def __str__(self):
#         return f"{self.title} by {self.author}"
#
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author
#
#         #gt = greater than, #add = add
#     def __lt__(self, other):
#         return self.num_pages < other.num_pages
#
#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author
#
#     def __getitem__(self, key):
#         if key == "title":
#             return self.title
#
#
#
# book1 = Book("The hobbit", "J.R.R. TOlkien", 310)
# book2 = Book("Harry potter", "J.K. Rowling", 223)
# book3 = Book("THe lion the witch and the wardrobe", "C.S. Lewis", 172)
#
# print(book1)
# print(book1 == book2)
# print(book2 < book3)
# print("lion" in book3)
#
# print(book1['title'])
# ------------------------------------------------------------------------------
# @property = Decorator used to define a method as a property. (accessed like an attribute)
#Benefit : Add additional logic when read, write or delete attributes. Gives you getter setter and deleter method.
#
# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#
#     @property
#     def width(self):
#         return f"{self._width:.1f}cm"
#
#     @property
#     def height(self):
#         return f"{self._height:.1f}cm"
#
#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater than 0")
#
#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._width = new_width
#         else:
#             print("Height must be greater than 0")
#
#     @width.deleter
#     def width(self):
#         del self._width
#         print("width has been deleted")
#
#
# rectangle = Rectangle(3,4)
#
# rectangle.width = 89
# print(rectangle.width, rectangle.height)
#
# del rectangle.width

# --------------------------------------------------------------------------------

#Decorator = Function that extends the behavior of another function w/o modifiyig
#base function. Pass the base function as an argument to the decorator.
#
# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("Added sprinkles")
#         func(*args, **kwargs)
#     return wrapper
#
# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("Fudge added")
#         func(*args, **kwargs)
#     return wrapper
#
# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"Here's your {flavor} ice cream.")
#
# get_ice_cream("vanilla")
# --------------------------------------------------------------------------
# exception = An event that interrupts the flow of a PROGRAM----
# try:
#     number = int(input("Enter a number: "))
#     print(1/number)
# except ZeroDivisionError:
#     print("You can't divide by zero, FFS")
# except ValueError:
#     print("Enter only numbers please")
# except Exception:
#     print("Something went wrong")
# finally:
#     print("DO some cleanup here")
# -------------------------------------------------------------------------------
import os
import json
import csv
#
# file_path = "file.txt"
#
# if os.path.exists(file_path):
#     print(f"THe location {file_path} exists")
#
#     if os.path.isfile(file_path):
#         print(f"{file_path} is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("Location does not exists")
# ------------------------------------------------------------------

#python writing files (.txt, .json, .csv)

# employees = {
#     "name": "Doge",
#     "age": 30,
#     "job": "cook"
# }
#
#
# txt_data = "I like pizza!"
file_path = "file.csv"
# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write("\n" + employee)
#             print(f"{employee} was written to {file_path}")
# except FileExistsError:
#     print("That file already exists!")
#
# try:
#     with open(file_path, "w") as file:
#         json.dump(employees, file, indent=4)
#         print(f"json file {file_path} was created")
# except FileExistsError:
#     print("That file already exists!")

employees = [["Name", "Age", "Job"],
            ["Doge", 25, "unfigo"],
            ["Buddy", 30, "ASSICURATORE"]]
try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file {file_path} was created")
except FileExistsError:
    print("That file already exists!")
