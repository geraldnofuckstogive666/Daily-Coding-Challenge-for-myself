#https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html



"""
check:
  https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
"""


#given that it is a 3x3 matrix


winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

    

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
    

def main():
    winner = winner_is(winner_is_also_1)
    
    if winner is not None:
        print(f"Winner is {winner}.")
        

if __name__ == "__main__":
    main()
