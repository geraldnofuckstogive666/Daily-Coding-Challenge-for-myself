#https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

"""
additional task for today since the last was kinda easy:
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, and 
ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock

#we can do like a twist with this challenge:
    1. Player vs bot (randomized selection using random modules)
    2. Player vs Player 
so we can prompt this before game start.
"""
import random
import sys

print("--Rock-Paper-Scissors--")

def get_choice(prompt):
    choice = input(prompt).lower()
    if choice not in choices:
        print("Invalid input. Try again.")
        return None
    return choice


choices = ["rock", "paper", "scissors"]
loses_to = {
    "rock": "paper",
    "scissors": "rock",
    "paper": "scissors"}


def solo_mode():
    print("""Choose:
          Rock
          Paper
          Scissors
          """)

    user = get_choice("Your choice: ")
    if not user:
        return

    computer = random.choice(choices)
    print(f"Computer chose {computer}")

    if user == computer:
        print("Draw!")
    elif loses_to[user] == computer:
        print("You lose!")
    else:
        print("You win!")

def multiplayer():
    print("""Choose:
        Rock
        Paper
        Scissors
        """)
    user1 = get_choice("Player 1: ")
    if not user1:
        return

    user2 = get_choice("Player 2: ")
    if not user2:
        return

    if user1 == user2:
        print("Draw!")
    elif loses_to[user1] == user2:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")


def mode():
    game_status = True
    while game_status:
        print("""Choose: \n
            Type 1 for Solo mode (vs Computer)
            Type 2 for Multiplayer
            """)
        try:
            user_input = int(input("Choose: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue
        
        if user_input == 1:
            solo_mode()

        elif user_input == 2:
            multiplayer()

        else:
            print("Invalid input. Try again.")

        print("""
            Do you want to start a new game?
            Type 1- Yes.
            Type 2- Exit
""")
        while True:
            try: 
                decider = int(input("Choose: "))
                
            except ValueError:
                print("Invalid input. Try again.")
                continue
            
            if decider == 2:
                game_status = False
                break
            elif decider == 1:
                break
            else:
                print("Invalid input. Try again.")
                continue

mode()
