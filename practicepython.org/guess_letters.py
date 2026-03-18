#https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html


def mask_word(word) -> str:
    return "_ " * len(word)

def update_mask(word, tracker):
    masked_word = ""
    for char in word:
        if tracker[char] == True:
            masked_word += f"{char} "
        else:
            masked_word += "_ "
    
    return masked_word.strip()


def word_to_dict(word):
    tracker = {}
    for char in word:
        tracker[char] = tracker.get(char, False)
    return tracker


def update_tracker(tracker, letter):
    return tracker.update({letter: True})


def main():
    guess_word = "EVAPORATE"
    print(mask_word(guess_word))
    tracker = word_to_dict(guess_word)

    while True:
        letter = input("Guess your letter: ").upper()

        if letter not in guess_word:
            print("Incorrect!")
            continue
        
        if tracker[letter] == True:
            print("You already guessed that letter correctly.")
            continue

        update_tracker(tracker, letter)
        print(update_mask(guess_word, tracker))


        if all(tracker.values()):
            print("Congratulations. You guessed it right!")
            break

if __name__ == "__main__":
    main()