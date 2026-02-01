#https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html


#comment for myself / thought process
"""
Okay so the problem is to ask a user for a number. 
then determine if even or odd then print out a message to the user.
Let's try to solve this.
    from what I learn on my algebra and discrete class: 
    even number is 2n - any integer multiplied by 2
        and we can work this around by just doing the modulus operator (n % 2)
    and odd number is 2n + 1 - so if we do a: 
        n % 2 = the output is 1 then that is odd
    so to sum it up, if the remainder is 0 it is even otherwise odd

    Now we can print out a message to the user.
-----
    But for this challenge let's try to do the extra challenge:
    1. different message for multiple of 4
    2. Ask the user for 2 numbers: 1 num to check (call it num), 
        the other num to divide by (call it check).
        Then, if check divides evenly into num, we tell that to user. (so print different message depends on the output)

    Let's try to solve.
        so on first extra challenge we can just add this on the above solution
        we can first determine if it's even and then we check if it's multiple by 4
        so like a nested if checker:
          n % 2 == 0: 
            (this is even right)
            then we can also check if it's multiple by 4 directly
            n % 4 == 0: coz multiple of 4 is just  4n
                then we printout a different message ponly for this
                I think that should do it.
        
        Now on the 2nd challenge, we can maybe do this after the first tasks above
        so the program would like have TWO main processes.
            1. first one, just asking ONE number from user then printout different messages for odd,even and multiples of 4s
            2. lastly, ask TWO number from user and print out different message depending on the divisbility.
         
            so to solve the 2nd challenge:
            we can ask for 2 numbers: num and check
            num:  it's like the dividend
            check:  more like the divisor 
            but the task is just to check if 'check' evenly divides into num
               so just num % check 
               and that should be it for the divisibility and we can determine it by the output and print out different messages.
    I think that should be it.
    Now onto the implementation, I will try to define a function for this:
                odd-even, multiplicity of 4, and divisibility of a num
                
        
    And let's do thissss.
"""

import sys


def is_even(num):
    return num % 2 == 0   #If this is true, then, it is even  and if not, then, we can just assume it is odd

def is_multifour(num):
    return num % 4 == 0


def is_divisible(a, b):
    if b == 0:
        return False
    else:
        return a % b == 0



def main():
    try:
        first = int(input("Number: "))
    except ValueError:
        sys.exit("Not a Number.")

    if is_even(first):
        if is_multifour(first):
            print(f"The number {first} is a multiple of 4.")
        else:
            print(f"The number {first} is an Even number.")
    else:    #for odd message
        print(f"The number {first} is an Odd number.")


    #now onto the second part
    print("\nPlease input TWO numbers...\n")

    try:
        num = int(input("First Number: "))
        check = int(input("Second Number: "))
    except ValueError:
        sys.exit("Not a number.")

    if is_divisible(num, check):
        print(f"The number {check} divides EVENLY into the number {num}.")
    else:
        print(f"The number {num} is not divisible by {check}.")


if __name__ == "__main__":
    main()