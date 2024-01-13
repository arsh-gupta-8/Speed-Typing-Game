from random import randint
import os
import curses
import colorama
from colorama import *

words = "words.txt"

colorama.init()
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET


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
    curses.wrapper(letter_getter, para)


def paragraph_collect(diff):
    all_sen = []
    with open(words, 'r') as doc:
        for sentence in doc:
            all_sen.append(sentence)
    para_index = randint(diff, diff + 9)
    para = all_sen[para_index]
    return para


def letter_getter(win, para):
    cc = 0
    chars = len(para)
    print(para)
    while 1:
        try:
            user_write = para.split("")
            key = win.getkey()
            if user_write[cc] == str(key):
                user_write[cc] = green + para[cc] + reset
            else:
                user_write[cc] = red + para[cc] + reset
                win.addstr(user_write[:cc] + user_write[cc + 1:])
                win.addstr(cc, str(key))
            cc += 1
        except Exception as e:
            pass


main()