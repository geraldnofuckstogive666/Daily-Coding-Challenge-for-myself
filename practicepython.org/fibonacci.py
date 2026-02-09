#https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html


"""
Write a program that asks the user how many Fibonnaci numbers to generate and 
then generates them. Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
 is the sum of the previous two numbers in the sequence. The sequence looks like this: 
 1, 1, 2, 3, 5, 8, 13, …)
 
 so the sequence we are using starts with 1, 1 and not 0, 1 ... then folowed by fib sequence



"""
from functools import lru_cache
import sys

@lru_cache(maxsize=None)
def fibonacci(num):
    if  num in (1, 2):
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


def fibonacci_sequential(num):
    return [fibonacci(n) for n in range(1, num + 1)]


try:
    user_input = int(input("Fibonacci numbers to generate: "))
    if user_input < 1:
        sys.exit("Invalid input.")
except ValueError:
    sys.exit("Invalid input.")

print(*fibonacci_sequential(user_input))







