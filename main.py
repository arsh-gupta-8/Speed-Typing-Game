import curses
from random import randint
from timeit import default_timer as timer
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
    wrapper(typing)


def typing(win):
    #COLOURS
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    green = curses.color_pair(1)
    red = curses.color_pair(2)
    white = curses.color_pair(3)
    yellow = curses.color_pair(4)

    win.clear()
    win.addstr(para)
    win.refresh()
    index, posx, posy = 0, 0, 0
    start, end = None, None
    timer_started = False
    run = True
    while run:
        try:
            key = win.getkey()
            if timer_started == False:
                start = timer()
                timer_started = True
            columns = curses.COLS
            if posx == columns:
                posx = 0
                posy += 1
            if key == "\n":
                break
            elif key in ("KEY_BACKSPACE", "\b", "\x7f"):
                index -= 1
                posx -= 1
                if posx < 0 and posy > 0:
                    posx = columns
                    posy -= 1
                win.addstr(posy, posx, para[index], white)
            else:
                if key == para[index]:
                    win.addstr(posy, posx, key, green)
                else:
                    win.addstr(posy, posx, key, red)
                posx += 1
                index += 1

            if index == len(para):
                end = timer()
                run = False
                win.addstr(6, 0, f"Your time was : {end-start} seconds", yellow)


            # testing purposes
            # win.addstr(10, 10, f"index - {index}, letter - {para[index]}, key - {key}, position(x, y) - {posy, posx}")

            win.refresh()

            if run == False:
                win.getch()

        except Exception as e:
            pass


main()
