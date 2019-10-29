# Program from Udemy course to make interactive dictionary
# Harry


#Import JSON
import json
from difflib import get_close_matches

# load JSON into var
data = json.load(open('data.json'))

# This is the main function that
# This function recieve a word as input
# And provide the difinition of that word
# by searching the data.json file
# Searches the JSON file for a match
# it will find closet match for you
#import difflib and get_close_matches to do
# this with

def check_word(word):
    word = word.lower()
    if word in data:
        return  data[word]
    elif len(get_close_matches(word, data.keys())) > 0:

        userInput = input('Did you mean %s instead? Enter Y, or N: ' % get_close_matches(word, data.keys())[0])
        if userInput == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif userInput  == 'N':
            return 'not a word in dictionary'
        else:
            return 'Confusing entry please check LOL'
    else:
        return 'not a word in dictionary'


input_word = input('enter word: ')

#python3 dictionary.py

output = check_word(input_word)
#print(check_word(input_word))
#checks if output is list
if type(output) == list:
    #print if its a list
    for item in output:
        print(item)
else:(output)
