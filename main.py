import curses
from random import randint
import time
import os
from curses import wrapper
import colorama
from colorama import *

words = "words.txt"

colorama.init()
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET


def main():
    global para
    print("Welcome to this game to check your typing speed")
    print("Lets begin")
    print("What difficulty would you like to play on Easy/Medium/Hard")
    choice = input("---   ")
    diff = None
    while diff == None:
        if choice.upper() == "EASY" or choice.upper() == "E":
            diff = 0
        elif choice.upper() == "MEDIUM" or choice.upper() == "M":
            diff = 10
        elif choice.upper() == "HARD" or choice.upper() == "H":
            diff = 20
        else:
            print("Sorry this option is unavailable")
            print("What difficulty would you like to play on Easy/Medium/Hard")
            choice = input("---   ")

    para = paragraph_collect(diff)
    game()


def paragraph_collect(diff):
    all_sen = []
    with open(words, 'r') as doc:
        for sentence in doc:
            sen = sentence.replace('\x00','').replace('\n','')
            if sen == "":
                pass
            elif sen[9] == "n":
                all_sen.append(sen[2:])
            else:
                all_sen.append(sen)
    para_index = randint(diff, diff + 9)
    para = all_sen[para_index]
    return para


def game():
    print(para)
    print("yo")
    print("Press enter to begin")
    input()
    wrapper(typing)


def typing(win):
    #COLOURS
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    green = curses.color_pair(1)
    red = curses.color_pair(2)

    win.clear()
    win.addstr(para)
    win.refresh()
    pos = 0
    run = True
    while run:
        try:
            key = win.getkey()
            win.refresh()
            time.sleep(5)
            return str(key)

        except Exception as e:
            pass


main()
