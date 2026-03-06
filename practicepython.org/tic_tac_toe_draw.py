#https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html


"""
#I think this is the checker
https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
"""

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]


def is_valid_move(row, col):
    return game[row][col] == 0


def prompt_move(prompt):
    while True:
        try:
            row, col = map(int, input(prompt).split(','))
        
        except ValueError:
            continue
        
        if 1 <= row <=3 and 1 <= col <= 3:
            return row - 1, col - 1
        


def main():
    print("Players must input row and column (in the format row,col)")
    players = ["Player 1", "Player 2"]
    turn = 0
    
    while True:
        row, col = prompt_move(f"{players[turn]}'s move: ")
        
        if is_valid_move(row, col):
            mark_move(players[turn], row, col)
            turn = (turn + 1) % 2
    
        for block in game:
            print(block)
        
        print()
    
        if is_no_move():
            break


        
def mark_move(who, row, col):
    if who == "Player 1":
        game[row][col] = "X"
    else:
        game[row][col] = "O"
    
    

def is_no_move():
    return 0 not in [cell for row in game for cell in row]


if __name__ == "__main__":
    main()


