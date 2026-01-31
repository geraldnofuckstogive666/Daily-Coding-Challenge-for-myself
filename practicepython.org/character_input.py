#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html


#Comment for myself / thought process
"""
so to compute on getting the year where someone turns to 100 years old 
it should be like
current_year + (100 - current_age?) = 100th_year? right?

if year is 2020 and im 20 years old currently 
100 - 20 = 80
   then we add this 80 (years it would take me to become 100 years old) to the current year
2020 + (100 - 20) = 2100 #so it means im turning 100 years old on the year 2100 

Problem is to ask for user for name and age and then print out the name and the year where user turns to 100 years old --- 
solve using input for name
then we try ask for user input for age  and we can convert that into int type

now using the makeup formula above ... we can get the current_year using datetime module
and then just plugin everything else on the formula so we get the 100th_year and we can then print out everything 
 and I think we should be done


implementation: keep it simple .. will not define a function for this
 
"""


import sys
from datetime import date


name = input("What's your name: ").strip().title()

try:
    age = int(input("Age: "))   

except ValueError:
    sys.exit("Invalid Age")


current_year = date.today().year
expected_year =  current_year + (100 - age)   #year where user turns 100 years old


print(f"{name}, You will turn 100 years old in the year {expected_year}.")