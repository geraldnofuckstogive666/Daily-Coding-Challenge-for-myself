#https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html



def print_grid(row=3, column=3, cell_char=' '):
    separator = ("+" + "---") * column + "+"
    print(separator)
    for _ in range(row):
        rows = ("|" + f" {cell_char} ") * column + "|"
        print(rows)
        print(separator)

def main():
    print("      ---Draw a Game Board---\n")
    try:
        x = int(input("How many rows: ").strip())
        y = int(input("How many columns: ").strip())
        
    except ValueError:
        print("Invalid input. Must be a number.")

    print_grid(x, y)
    
  

if __name__ == "__main__":
    main()
