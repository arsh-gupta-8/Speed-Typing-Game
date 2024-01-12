from random import randint
import os
import curses
import colorama
from colorama import *

words = "words.txt"

colorama.init()
red = Fore.RED

print(red + "some text")

def main():
    print("Welcome to this game to check your typing speed")
    print("Lets begin")
    print("What difficulty would you like to play on Easy/Medium/Hard")
    choice = input("---   ")
    diff = None
    while diff == None:
        if choice.upper() == "EASY" or choice.upper() == "E":
            diff = 0
        elif choice.upper() == "MEDIUM" or choice.upper() == "M":
            diff = 11
        elif choice.upper() == "HARD" or choice.upper() == "H":
            diff = 22
        else:
            print("Sorry this option is unavailable")
            print("What difficulty would you like to play on Easy/Medium/Hard")
            choice = input("---   ")

    paragraph = paragraph_collect(diff)
    game(paragraph)

def game(para):
    os.system('cls')
    user_write = para
    letter = curses.wrapper(main)


def paragraph_collect(diff):
    all_sen = []
    with open(words, 'r') as doc:
        for sentence in doc:
            all_sen.append(sentence)
    para_index = randint(diff, diff+9)
    para = all_sen[para_index]
    return para

def letter_getter(win):
    win.clear()
    while 1:
        try:
            key = win.getkey()
            return str(key)
        except Exception as e:
           pass

# main()