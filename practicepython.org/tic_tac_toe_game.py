#Part 1 - https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

#Part 2- https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html

#Part 4 (This challenge) - https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html

game = [[0, 0, 0],
	[0, "X", 0],
	[0, 0, 0]]



#check first before update
def is_valid_move(row, col):
    return game[row][col] == 0

#check after we update the board
def is_no_move():
    return 0 not in [cell for row in game for cell in row]


def mark_move(player, row, col):
    if player == "Player 1":
        game[row][col] = "X"
    else:
        game[row][col] = "O"
        
        
def print_grid(game):
    separator = ("+" + "---") * 3 + "+"
    print(separator)
    for row in game:
        elements = ' | '.join(map(str,row))
        print(f"| {elements} | ")
        print(separator)


#----------------------------------


#-------------checker for winner----------------
def row_checker(row: list) -> int:
    values = set(row)

    if len(values) != 1:
        return None

    winner = values.pop()

    if winner == 0:
        return None

    return winner


def diagonal_checker(matrix: list) -> int:
    size = len(matrix)

    diag1 = [matrix[i][i] for i in range(size)]
    diag2 = [matrix[i][size - 1 - i] for i in range(size)]

    for diag in (diag1, diag2):
        values = set(diag)
        if len(values) == 1:
            winner = values.pop()
            if winner != 0:
                return winner

    return None


def transposed_matrix(matrix: list) -> list:
    return [list(row) for row in zip(*matrix)]


def winner_is(matrix: list) -> int:
    for row in matrix:
        result = row_checker(row)
        if result is not None:
            return result

    for column in transposed_matrix(matrix):
        result = row_checker(column)
        if result is not None:
            return result

    result = diagonal_checker(matrix)
    if result is not None:
        return result

    return None
    

def final_check(matrix):
    winner = winner_is(matrix)
    if winner is not None:
        print(f"Winner is {winner}.")
    else:
        print("No winner.")
        
        



    
