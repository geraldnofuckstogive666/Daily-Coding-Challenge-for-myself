#https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html


def max_of_three(a, b, c):
    largest = a if a > b else b
    return largest if largest > c else c
    
def main():
    #test the max_of_three function
    a = 10
    b = 11
    c = 7
    
    largest = max_of_three(a, b, c)
    
    print(largest)
    
if __name__ == "__main__":
    main()


