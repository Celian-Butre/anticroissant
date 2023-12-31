from pynput.keyboard import Key, Listener, Controller
import time
keyboard = Controller()

typed_characters = []

def backspace():
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

def printWord(word):
    for x in word:
        if x == "·":
            keyboard.type("\u00B7") #·
            #keyboard.type("\u30FB") #・ 
        else:
            keyboard.press(x)
            keyboard.release(x)

def on_press(key):
    global typed_characters
    try:
        # Check if the pressed key is a printable character
        char = key.char
        if char is not None:
            # Add the character to the typed_characters list
            typed_characters.append(char)
            # Keep only the last 100 characters
            typed_characters = typed_characters[-100:]
            # Check if the forbidden word is present
            typed_text = (''.join(typed_characters)).lower()
            #print (typed_text)
            if 'croissa' in typed_text:
                for i in range(20):
                    backspace()
                    time.sleep(0.1)
                printWord("Bro Stop.")
                # You can add your handling logic here (e.g., prevent further input)

    except AttributeError:
        # Handle special keys (e.g., Backspace)
        if key == key.backspace:
            # Remove the last character if Backspace is pressed
            if typed_characters:
                typed_characters.pop()

def on_release(key):
    pass

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

