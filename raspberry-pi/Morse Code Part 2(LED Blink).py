import board
import pwmio
import time

buzzer = pwmio.PWMOut(board.GP17, duty_cycle=0, frequency=1440)
OFF = 0
ON = 2**15
DOT = 0.05
DASH = 3*DOT

 
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
BEEP = {'.': DOT , '-': DASH}

while True:
    Input = input()
    x = Input.upper()
    if Input == str("-q"):
        break
    for letter in x:
        if letter == " ":
            time.sleep(7*DOT)
            print("/", end=" ")
            continue
        print(MORSE_CODE[letter], end=" ")
        for pulse in MORSE_CODE[letter]:
            # print(f"pulsing for {pulse} for letter {letter}")
            buzzer.duty_cycle = ON
            time.sleep(BEEP[pulse])
            buzzer.duty_cycle = OFF
            time.sleep(DOT)
        time.sleep(3*DOT)
    print()
    
