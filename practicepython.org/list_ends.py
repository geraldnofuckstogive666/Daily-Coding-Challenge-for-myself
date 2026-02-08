#https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

"""
Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) and makes a new 
list of only the first and last elements of the given list. 
For practice, write this code inside a function.
"""

def list_ends(lst):
    if len(lst) == 1:   #list is got only 1 element so I can only return itself
        return lst
    elif len(lst) < 1: #so it means I cant return a first and last elements because there is nothign to return
        return []
    
    return [lst[0],lst[-1]]

a = [5, 10, 15, 20, 25]
print(list_ends(a))