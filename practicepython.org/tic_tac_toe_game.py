#Part 1 - https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

#Part 2- https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html

#Part 4 (This challenge) - https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html

#----------------print 3x3 grid --------------
def print_grid(gridsize=3, cell_char=0):
    separator = ("+" + "---") * gridsize + "+"
    print(separator)
    for _ in range(gridsize):
        rows = ("|" + f" {cell_char} ") * gridsize + "|"
        print(rows)
        print(separator)
#---------------print 3x3 grid-----------------


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


#------------------checker for winner----------


def main():
    print_grid()

if __name__ == "__main__":
    main()
    

    
