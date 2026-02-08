#https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

#comment for myself / task / thought process
"""
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 

so a prime number is 
a natural number greater than 1 that is not a product of two smaller 
natural numbers.

so it's prime if I can only do like 1 * itself = itself right?
                        and I cant get any other number for it to be itself

                        
welp i watched a video on how square roots can help in checking if a number is prime
https://www.youtube.com/watch?v=dl7LLYw-xbQ
 so imma try to apply hopefully correct what i've learned from it

  
so basically if I cant find a number from 2 up until its square root (or closest natural number)
        to be a divisor for that number then it is a prime.



"""
import sys
from math import isqrt

def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True

 
    for n in range(2, isqrt(num) + 1):
        if num % n == 0:
            return False
    return True

try:
    num = int(input("Enter a number: "))
except ValueError:
    sys.exit("Not a valid number.")


if is_prime(num):
    print(f"The number {num} is a prime number.")
else:
    print(f"The number {num} is NOT a prime number.")