#https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

#comment for myself / thought process
"""
Create a program that asks the user for a number and then prints out a list of all the 
divisors of that number. (If you don’t know what a divisor is, it is a number that divides
evenly into another number. For example, 13 is a divisor of 26 
because 26 / 13 has no remainder.)

So I would assume that it is for positive numbers and 
the list of divisors are numbers greater than 1  and until the number itself
that are evenly divisible to the number from user input

Sol. 
    create an empty list
    ask user for a number and convert to int <- only positive I guess 
    and then use that number as range 1 up to n
    in python i believe it's like range(1, n + 1) since it's not inclusive 
    then we can loop through these numbers and add all the numbers that can evenly divide into the user's number into our list
    and then lastly print out all the elements in the list using a for loop
    and that should be it

Implementation:
    Just a simple straightforward approach implementation of the above solution


"""
from sys import exit


try:
    user_input = int(input("Enter a number: "))
except ValueError:
    exit("Not a number.")

divisor_list = []

for n in range(1,user_input):
    if user_input % n == 0:
        divisor_list.append(n)



for n in divisor_list:
    print(n)