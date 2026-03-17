#https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
#words from: http://norvig.com/ngrams/sowpods.txt

import random


def fetch_words(file_name: str) -> list[str]:
    try:
        with open(file_name, 'r') as open_file:
            return [line.strip() for line in open_file]
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")

def pick_word(words: list[str])-> str:  #random word
    return random.choice(words)


def main():
    FILE_NAME = 'sowpods_dictionary.txt'
    sowpods = fetch_words(FILE_NAME) 
    print(pick_word(sowpods))


if __name__ == "__main__":
    main()
