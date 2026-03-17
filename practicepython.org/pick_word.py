#https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
#words from: http://norvig.com/ngrams/sowpods.txt

import random

FILE_NAME = 'sowpods_dictionary.txt'

def fetch_word(file_name):
    words = []

    with open(file_name, 'r') as open_file:
        for line in open_file:
            words.append(line.strip())
    return words

def pick_word(words: list)-> str:  #random word
    return random.choice(words)



def main():
    sowpods = fetch_word(FILE_NAME) 
    print(pick_word(sowpods))



if __name__ == "__main__":
    main()





