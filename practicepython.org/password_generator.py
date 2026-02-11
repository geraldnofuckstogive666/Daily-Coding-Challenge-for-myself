#https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

"""
Note: this is a 4-chili exercise, not because it introduces a concept, but because this exercise is more like
 a project. Feel free to skip this and come back when you’re more ready!

Write a password generator in Python. Be creative with how you generate 
passwords - strong passwords have a mix of lowercase letters, 
uppercase letters, numbers, and symbols. The passwords should be random, 
generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. 
For weak passwords, pick a word or two from a list.
"""
import string
import sys
import time
import random



def get_choice(prompt):
    password_class = ["weak", "medium", "strong"]
    choice = input(prompt).strip().lower()
    if choice not in password_class:
        sys.exit("Invalid input. Try again.")
    return choice


def main():
    start_time = time.perf_counter()
    print("""---Password Generator---
Choose your password stength:
    Weak
    Medium
    Strong""")
    password = password_classifier(get_choice("Password Strength: "))
    
    print(f"Password Generated: {password}")

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")



def password_classifier(strength):
    if strength == "weak":
        return weak_generator()
    elif strength == "medium":
        return medium_generator()
    elif strength == "strong":
        return strong_generator()
    else:
        return None

def weak_generator():
    words = ["apple", "banana", "berry", "cherry", "qwerty", "john", "monday"]
    digits = string.digits
    n = random.randint(1,7)
    return random.choice(words) + digits[n:n+3]



def medium_generator():
    word = random.choice(["apple", "banana", "berry", "cherry", "qwerty", "john", "monday"]).title()
    color = random.choice(["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "gray", "cyan"]).title()
    n = random.randint(1,7)
    digit = string.digits[n:n+3]
    password = [word, color, digit]
    random.shuffle(password)
    sep = random.choice(["!","#","@"])
    return sep.join(password)



def strong_generator():
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation
    password_length = random.randint(12,18)
    password = []
    a, b, c = number_splitter(password_length)
    for _ in range(a):
        password.append(random.choice(letters))
    for _ in range(b):
        password.append(random.choice(digits))
    for _ in range(c):
        password.append(random.choice(specials))
    random.shuffle(password)
    return "".join(password)

def number_splitter(num, n=3):
    points = sorted(random.sample(range(1, num), n-1))
  
    parts = []
    prev_point = 0
    for point in points:
        parts.append(point - prev_point)
        prev_point = point
    parts.append(num - prev_point) 

    return parts

if __name__ == "__main__":
    main()