#part 1 - https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
#github: https://github.com/geraldnofuckstogive666/Daily-Coding-Challenge-for-myself/blob/main/practicepython.org/pick_word.py

#part 2 - https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html
#github: https://github.com/geraldnofuckstogive666/Daily-Coding-Challenge-for-myself/blob/main/practicepython.org/guess_letters.py

#part 3 (this challenge) - https://www.practicepython.org/exercise/2017/01/10/32-hangman.html
import sys
import random

FILE_NAME = 'sowpods_dictionary.txt'

def fetch_words(file_name: str) -> list[str]:
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return []

def pick_word(words: list[str])-> str | None:  #random word
    if not words:
        return None
    return random.choice(words)


def mask_word(word) -> str:
    return "_ " * len(word)

def update_mask(word, tracker):
    return " ".join(char if tracker[char] else "_" for char in word)

def word_to_dict(word):
    return  {char: False for char in word}







def main():
    words = fetch_words(FILE_NAME)
    guess_word = pick_word(words)
    tracker = word_to_dict(guess_word)
    guessed_letters = set()
    guesses_left = 6
    
    print(guess_word)
    print(mask_word(guess_word))

    while True:
        if guesses_left <= 0:
            print("Game Over.")
            break

        letter = input("Guess your letter: ").upper()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            continue

        if letter in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(letter)

        if letter not in guess_word:
            print("Incorrect!")
            guesses_left -= 1
            print(f"You have {guesses_left} {"guesses" if guesses_left > 1 else "guess"} left.")
            continue

        tracker[letter] = True
        print(update_mask(guess_word, tracker))

        if all(tracker.values()):
            print("Congratulations. You guessed it right!")
            break
    

    
    retry_again = input("Play again? Y/N: ").upper()
    if retry_again == "Y":
        main()
    elif retry_again == "N":
        sys.exit("Thanks for playing. Game Terminated.")
    else:
        sys.exit("Not quite right. Game Terminated.")
        

if __name__ == "__main__":
    main()