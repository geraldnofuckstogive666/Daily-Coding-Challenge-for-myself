#https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html


def mask_word(word) -> str:
    return "_ " * len(word)

def update_mask(word, tracker):
    return " ".join(char if tracker[char] else "_" for char in word)

def word_to_dict(word):
    return  {char: False for char in word}


def main():
    guess_word = "EVAPORATE"
    tracker = word_to_dict(guess_word)
    guessed_letters = set()

    print(mask_word(guess_word))

    while True:
        letter = input("Guess your letter: ").upper()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            continue

        if letter in guessed_letters:
            print("You already guessed that letter.")
        
        guessed_letters.add(letter)

        if letter not in guess_word:
            print("Incorrect!")
            continue

        tracker[letter] = True
        print(update_mask(guess_word, tracker))

        if all(tracker.values()):
            print("Congratulations. You guessed it right!")
            break


if __name__ == "__main__":
    main()