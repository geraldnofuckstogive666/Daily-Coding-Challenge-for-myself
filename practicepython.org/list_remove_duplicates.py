#https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html


"""
Write a program (function!) that takes a list and returns a new list 
that contains all the elements of the first list minus all the duplicates.

Extras:
Write two different functions to do this - one using a loop and 
constructing a list, and another using sets.
"""
from random import randint

def remove_duplicates(lst):
    return list(set(lst))

#extra
def remove_duplicate_with_loop(lst):
    new_list = []
    for n in lst:
        if n not in new_list:
            new_list.append(n)
    return sorted(new_list)


sample = [randint(1,20) for _ in range(21)]
print(sample)
print("1st function:", *remove_duplicates(sample))
print("2nd function:", *remove_duplicate_with_loop(sample))