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

def scrape_webpage(url: str):
    # objective: scrape info from given URL's webpage, get webpage title and contents, return this info
    html_content = get_request(url) # step 1: read in website URL, get its HTML content using a GET request
    webpage_content = [] # result list where webpage title and content will go
    # step 2: create a BeautifulSoup instance. Then, pass it our URL's HTML content to be parsed with BeautifulSoup's LXML parser
    tomato_soup = BeautifulSoup(html_content, 'lxml')
    webpage_title = tomato_soup.find('head').find('title').text # step 3: get webpage's title from the 'head' tag
    webpage_content.append(webpage_title) # step 4: add webpage title to list of webpage content
    webpage_text = tomato_soup.find('body') # step 4: get webpage's text content (tags, info, etc.) from the 'body' tag
    for content_tag in webpage_text.find_all(True):
        # step 5: iterate through ALL tags in webpage body, extract text from each tag, add that text to 'webpage_content' list
        current_text = tomato_soup.find_all(content_tag) # ALL matches for current HTML tag
        if len(current_text) > 1:
            # if length of 'current_text' list is over 1, then we have multiple matches for given tag
            for str in current_text:
                webpage_content.append(str.text) # append each tag's text
        else:
            # else, we either have one match or no matches for given tag
            match = tomato_soup.find(content_tag).text
            webpage_content.append(match) # append single match (or result of null) to result list
    return webpage_content


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrape_webpage('http://google.com') # should print the title of given URL

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
