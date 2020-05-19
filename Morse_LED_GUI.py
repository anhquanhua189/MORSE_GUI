## import our libs ##
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

##declar our dot value - which is 1 sec
DOT_VALUE = 1 

## our LED hardware ##
red = LED(4)

## our morse code dict ##
CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}
## our functions ##
#blink the Led to represent either a dot or a dash
def blinkLed(string):
    if string == "dot":
        red.on()
        time.sleep(DOT_VALUE)
        red.off()
        time.sleep(DOT_VALUE)
    if string == "dash":
        red.on()
        time.sleep(DOT_VALUE*3)
        red.off()
        time.sleep(DOT_VALUE)
def blinkWord():
    word = wordEntry.get()
    wordList = list(word)
    for letter in wordList:
        for char in CODE[letter.upper()]:
            if char == '-':
                blinkLed("dash")
            elif char == '.':
                blinkLed("dot")
            else: ##a space is 7 dots##
                time.sleep(DOT_VALUE*7)
        time.sleep(DOT_VALUE*3)
        
## create a function to limit the size of our entry    
def limitSizeWord(*args):
    value = wordValue.get()
    if len(value) > 12:
        wordValue.set(value[:12])
## GUI Design ##
win = Tk()
win.title("Morse LED Blinking")
guiFont = tkinter.font.Font(family = 'Helvetica',
                            size = 12, weight = "bold")
button = Button(win, text = 'Blink', font = guiFont,
                    command = blinkWord, bg = 'bisque',height = 1,
                    width = 12)
Label(win, text='Your word: ').grid(row = 0, column = 0)
wordValue = StringVar()
##string var is tracked by the use of trace
##stringVar() will call for limitSizeWord any time we make a change
wordValue.trace('w', limitSizeWord)
##set the wordEntry inside our text box
wordEntry = Entry(win, width = 13, textvariable = wordValue)
wordEntry.grid(row = 0, column = 1)

Label(win, text ='Text limit is 12 char.').grid(row = 0, column = 2)
button.grid(row = 1, column = 1)
