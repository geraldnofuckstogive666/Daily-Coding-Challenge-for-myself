#https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


user_input = input("Enter a string: ").lower()
print(f"The string {user_input} is {("a Palindrome" if is_palindrome(user_input) else "Not a Palindrome")}")