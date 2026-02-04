#https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

#comment for myself / tasks / thought process
"""
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the 
elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras: 
Randomly generate two lists to test this
Write this in one line of Python 
(don’t worry if you can’t figure this out at this point - we’ll get to it soon)

Sol.
    on this particular problem (basic problem), I can think of 2 solution
        1. create an empty list then do like a loop comparison for elements in the two lists and if it exists on both we add that to the empty list
            if and only if it does not exist on empty list we created to ensure it is unique
        2.  is to use set() on both lists, this way we have a unique elements on both the lists (which is now a set object)
            and since it is now a set we can use the intersection method or operator (&) and store the elements on a variable
            and then lastly convert it back to a list 
Extras sol.
    1. on that task about randomly generating two list to test, we can try to user the randint from random module, list and range() function for this
        then, do apply any of the above solution to test.
    2. As for the write this in one line of python, I am not sure if that includes the list intialization 
    but imma just  assume that it's not included and only refering the logic (solution) to the problem,
    so we can initialize a list (maybe still use the randint from random) maybe just use the randomly generated list from the 1st extra challenge 
    then do a print then unpack of the list on a link comprehension with applied solution logic


so on the implementation I think i would try to implement the two solutions above just to see
if both actually works    
    so the program would be like
        basic problem solution, but i will be using the list given above
            1. first sol
            2. 2nd sol
        
        extras
            1. solution using the 2 sols applied on a randomly generated list
            2. using the randomly generated list from the first extra challenge, we do a one-liner
    
lezzdothis
    """
from random import randint

#basic problem solution
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
#first solution
for n in a:
    if n in b and n not in c:
        c.append(n)

print("first solution:", c)

#second solution/ still using the same list
d = list(set(a) & set(b))
print("second solution:", d)

print("\nExtras")
#first extra challenge solution
list1 = [randint(1,50) for _ in range(20)]
list2 = [randint(1,50) for _ in range(20)]
list3 = []
print("first random list:",list1)
print("second random list:",list2)
#sol1
for n in list1:
    if n in list2 and n not in list3:
        list3.append(n)


print("first solution:", list3)

#second solution/ still using the same list
list4 = list(set(list1) & set(list2))
print("second solution:", list4)

#one-liner challenge using the randomly generated list
print("\nOne-liner:", list(set(list1) & set(list2)))
