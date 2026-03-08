#Part 1 - https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

#Part 4 (This challenge) - https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html

def print_grid(gridsize, cell_char=0):
    separator = ("+" + "---") * gridsize + "+"
    print(separator)
    for _ in range(gridsize):
        rows = ("|" + f" {cell_char} ") * gridsize + "|"
        print(rows)
        print(separator)

def main1():
    print("      ---Draw a Game Board---\n")
    try:
        x = int(input("Grid size: ").strip())
    except ValueError:
        print("Invalid input. Must be a number.")
    print_grid(x)
    #---------------------Drawing a board game
  
