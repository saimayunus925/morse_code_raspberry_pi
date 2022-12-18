# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests # 'requests' library for handling HTTP requests/responses in Python (HTTP responses tend to have HTML content)
from bs4 import BeautifulSoup # 'BeautifulSoup' library for scraping websites for specific info

def python_morse_code_dictionary() -> dict:
    # returns Python 'English to Morse Code' dictionary
    return {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',

        ' ': '/'
    }
    # source for this dictionary: https://stackoverflow.com/questions/32094525/morse-code-to-english-python3

def translate_morse(sentence: str) -> str:
    # translate given English string into Morse code, return the Morse code string
    uppercase_sentence = sentence.upper() # we'll translate this string so there's no conflicts with the dictionary
    morse_dictionary = python_morse_code_dictionary() # a copy of our Python Morse code dictionary
    result = [] # each char's Morse counterpart goes here to form the full 'string'
    for ch in uppercase_sentence:
        morse_char = morse_dictionary[ch] # getting current char's Morse counterpart
        result.append(morse_char) # adding current Morse char to 'result' list
    return ' '.join(result) # join list of Morse chars into a space-separated string, return the result

def get_request(url: str):
    # reads in website URL, returns its HTML content as a GET request
    return requests.get(url).text

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
