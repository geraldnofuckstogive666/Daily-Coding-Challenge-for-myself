#https://www.practicepython.org/exercise/2014/11/11/20-element-search.html


"""
Docstring for element_search
Write a function that takes an ordered list of numbers (a list where the elements 
are in order from smallest to largest) and another number. The function 
decides whether or not the given number is inside the list and returns 
(then prints) an appropriate boolean.

Extras:

Use binary search.
"""
from random import randint
#binary search for ordered list ---

a = sorted([randint(1,100) for _ in range(100)])
b = sorted([5, 33, 52, 64, 72, 5, 24, 75, 47, 2, 58, 32, 64, 41, 59, 46, 21, 39, 53, 62, 1, 37, 12, 52, 34, 48, 99, 100, 70, 13, 97, 35, 67, 49, 34, 100, 75, 69, 99, 83, 65, 55, 76, 52, 82, 26, 66, 89, 61, 22, 66, 25, 64, 49, 61, 35, 64, 62, 52, 99, 81, 37, 4, 38, 70, 49, 73, 30, 49, 91, 17, 84, 2, 33, 42, 86, 70, 50, 55, 48, 66, 83, 8, 82, 35, 81, 40, 15, 98, 61, 16, 16, 51, 75, 72, 42, 86, 51, 25, 94])


def binary_search(lst, n) -> bool:
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == n:
            return True
        
        elif lst[mid] < n:
            low = mid + 1
        else:
            high = mid - 1

    return False

def main():
    num = 50
    print("on list A:", binary_search(a, num))
    print("on list B:",binary_search(b, num))

if __name__ == "__main__":
    main()