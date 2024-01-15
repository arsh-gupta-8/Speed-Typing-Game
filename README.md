# Speed-Typing-Game
This game gives you a piece of text for you to type and times you on how long it takes to type it. Then based on the time it can estimate how many words you can type in a minute (WPM) and so on.

## Rules
This game is inspired by popular online speed typing test. Similarly, in this game you are given a random paragraph which you have to follow along and type as **fast** as you can! There are also set difficulties _(easy, medium and hard)_, if you feel like challenging yourself you can try harder difficulties. Making mistakes can be quite punishing to your final score (your WPM) unless you make corrections.

## More About the Code

### Modules
The most important module I used for this game was the curses module which allows me to make a new window to work on with useful features such as key detection and colour

~~~python
import curses
from random import randint
from timeit import default_timer as timer
import math
from curses import wrapper
import colorama
from colorama import *
~~~

### Calculation for WPM
To calculate the words per minute I use a slightly different approach which is to check the number of letters correctly input by the user and then dividing it by the average word length and the time taken. This would result in the number of words written per second fo which I multiply by 60 to turn it into words per minute. 

~~~python
# index - the total nuber of characters in the paragraph
# wrongs - list containing wrong inputs
# avg_words_len - average length of a word in the paragraph
# (end - start) - the time taken to finish writing the paragraph

wpm = (index - len(wrongs)) / (avg_word_len * (end - start))
~~~