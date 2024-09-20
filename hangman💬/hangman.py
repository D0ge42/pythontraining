import random
from wordslist import words
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

RESET = "\033[0m"

index = 0
guessed = []
word_to_guess = random.choice(words)
guesses = 0
ascii_art = {
    0: (),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\"),
    7: (" |  ",
        " o ",
        "/|\\",
        "/ \\")
}

def print_ascii_art(ascii_art, key):
    for item in ascii_art[key]:
        print(item)

def list_to_string(lista, string):
    for item in lista:
        string+=item
    return string

def initialize_list(guess_list,string):
    for letter in string:
        guess_list.append("")

initialize_list(guessed,word_to_guess)

def find_indexes(str,x):
    indices = [index for index, char in enumerate(str) if char == x]
    for item in indices:
        item = int(item)
    return indices


def better_list(guessed):
    empty_string = ""
    for item in guessed:
        empty_string += "-"
    return empty_string

strong = better_list(guessed)
print(f"{YELLOW}The word is {strong}. {len(strong)} letters{RESET}")
while True:
    print()
    if strong == word_to_guess:
        print(f"{GREEN}---✅CONGRATZ!!! YOU FOUND THE HIDDEN WORD!✅---{RESET}")
        print()
        choice = input(f"{BRIGHT_BLUE}Do you wanna play again?(Y/N): {RESET} ")
        match choice:
            case "y":
                index = 0
                guessed = []
                word_to_guess = random.choice(words)
                initialize_list(guessed, word_to_guess)
                strong = ""
                strong = better_list(guessed)
                print(f"{YELLOW}The word is {strong}. {len(strong)} letters{RESET}")
            case "n":
                break
    letter = input("Enter a letter: ").lower()
    if letter.isdigit() or letter == "":
        print("Letter was not valid")
        continue
    if len(letter) > 1:
        print("Only one letter allowed")
    else:
        if letter in word_to_guess:
            index_letter = find_indexes(word_to_guess,letter)
            strong = list(strong)
            for indexes in index_letter:
                strong[indexes] = letter
            # strong[index_letter] = letter
            strong = ''.join(strong)
            print(f"📌{CYAN}The letter{RESET} {BRIGHT_MAGENTA}{letter}{RESET} {CYAN}is in the word to guess!{RESET}📌 ")
            print(strong)
        else:
            print(f"❌The letter {letter} could not be found in the hidden word!❌ ")
            index += 1
            if index ==7:
                print_ascii_art(ascii_art,index)
                print(f"{RED}-----YOU LOST-----{RESET}")
                print(f"💬The hidden word was {word_to_guess}💬")
                choice = input(f"{BRIGHT_BLUE}Do you wanna play again?(Y/N):{RESET} ")
                match choice:
                    case "y":
                        index = 0
                        guessed = []
                        word_to_guess = random.choice(words)
                        initialize_list(guessed, word_to_guess)
                        strong = ""
                        strong = better_list(guessed)
                        print(f"{YELLOW}The word is {strong}. {len(strong)} letters{RESET}")
                    case "n":
                        break
                    case _:
                        index = 0
                        guessed = []
                        word_to_guess = random.choice(words)
                        initialize_list(guessed, word_to_guess)
                        strong = ""
                        strong = better_list(guessed)
                        print(f"{YELLOW}The new word is {strong}. {len(strong)} letters{RESET}")
            else:
                print_ascii_art(ascii_art,index)
