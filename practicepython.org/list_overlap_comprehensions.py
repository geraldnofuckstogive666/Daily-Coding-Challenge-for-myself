#https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html


"""
This is just the same with the exercise 5 and 7 
so nothing to note much in here:
goals:
    write a program that return a list that contains only the elements that 
    are common between the lists (without duplicates). works on different sizes
1. for a given lists
2. for a randomly generated lists
"""
from random import randint


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("--for the given list--")

c = [n for n in a if n in b] #common elements list

def duplicate_remover(lst):
    return list(set(lst))

print(duplicate_remover(c))

print("\nfor the pure random list")

random1 = [randint(1, 100) for _ in range(randint(5, 21))]
random2 = [randint(1, 100) for _ in range(randint(5, 21))]
print("first random list:", random1)
print("second random list:", random2)

print(list(set(random1) & set(random2)))