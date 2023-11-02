import board
import pulseio
import time
buzzer = pulseio.PWMOut(board.GP17, variable_frequency=True)
buzzer.frequency = 440
OFF = 0
ON = 2**15
DOT = 0.25
DASH = 0.75

# Dictionary representing the morse code chart
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ',':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}
BEEP = {'.-':(DOT, DASH) , '-...':(DASH, DOT, DOT, DOT),
    '-.-.':(DASH, DOT, DASH, DOT), '-..':(DASH, DOT, DOT),'.':(DOT),
    '..-.':(DOT, DOT, DASH, DOT), '--.':(DASH, DASH, DOT), '....':(DOT, DOT, DOT, DOT),
    '..':(DOT, DOT), '.---':(DOT, DASH, DASH, DASH), '-.-':(DASH, DOT, DASH),
    '.-..':(DOT, DASH, DOT, DOT), '--':(DASH, DASH), '-.':(DASH, DOT),
    '---':(DASH, DASH, DASH), '.--.':(DOT, DASH, DASH, DOT), '--.-':(DASH, DASH, DOT, DASH),
    '.-.':(DOT, DASH, DOT), '...':(DOT, DOT, DOT), '-':(DASH),
    '..-':(DOT, DOT, DASH), '...-':(DOT, DOT, DOT, DASH), '.--':(DOT, DASH, DASH),
    '-..-':(DASH, DOT, DOT, DASH), '-.--':(DASH, DOT, DASH, DASH), '--..':(DASH, DASH, DOT, DOT),
    '.----':(DOT, DASH, DASH, DASH, DASH), '..---':(DOT, DOT, DASH, DASH, DASH), '...--':(DOT, DOT, DOT, DASH, DASH),
    '....-':(DOT, DOT, DOT, DOT, DASH), '.....':(DOT, DOT, DOT, DOT, DOT), '-....':(DASH, DOT, DOT, DOT, DOT),
    '--...':(DASH, DASH, DOT, DOT, DOT),'---..':(DASH, DASH, DASH< DOT, DOT), '----.':(DASH, DASH, DASH, DASH, DOT),
    '-----':(DASH, DASH, DASH, DASH, DASH), '--..--':(DASH, DASH, DOT, DOT, DASH, DASH), '.-.-.-':(DOT, DASH, DOT, DASH, DOT, DASH),
    '..--..':(DOT, DOT, DASH, DASH, DOT, DOT), '-..-.':(DASH, DOT, DOT, DASH, DOT), '-....-':(DASH, DOT, DOT, DOT, DOT, DASH),
    '-.--.':(DASH, DOT, DASH, DASH, DOT), '-.--.-':(DASH, DOT, DASH, DASH, DOT, DASH)}

while True:
    Input = input()
    x = Input.upper()
    for letter in x:
        print(MORSE_CODE[letter], end=" ")
        buzzer.duty_cycle = ON
        time.sleep(BEEP[MORSE_CODE[letter]])
        buzzer.duty_cycle = OFF
    if Input == str("-q"):
        break
