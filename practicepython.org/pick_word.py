#https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
#words from: http://norvig.com/ngrams/sowpods.txt

import random

FILE_NAME = 'sowpods_dictionary.txt'

def fetch_words(file_name: str) -> list[str]:
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return []

def pick_word(words: list[str])-> str:  #random word
    if not words:
        return None
    return random.choice(words)


def main():
    sowpods = fetch_words(FILE_NAME) 
    word = pick_word(sowpods)

    if word is None:
        print("No words available.")
    else:
        print(word)


if __name__ == "__main__":
    main()
