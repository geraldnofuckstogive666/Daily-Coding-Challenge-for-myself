#https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html


"""
Generate a random number between 1 and 9 
(including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)
"""

from random import randint
number_to_be_guessed = randint(1,9)

guess_count = 0
print("---= Guess the number 1-9 =---")
while True:
    user_input = input("Please enter a number or type 'exit': ")
    if user_input == "exit":
        break
    try:
        guess = int(user_input)
    except ValueError:
        continue

    guess_count += 1
    if guess == number_to_be_guessed:
        print("You are right!")
        print(f"You guessed the number in {guess_count} {('attempt' if guess_count ==  else 'attempts')}.")
        break
    elif guess < number_to_be_guessed:
        print("Too low!")
    else:
        print("Too high!")

