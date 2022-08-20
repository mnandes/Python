#Get Python Version
import sys

print("Python Version\n" + sys.version)

###################################################################
#Get Current Date and Time
import datetime

now = datetime.datetime.now()

print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

###################################################################
#Calculate circle area from radius
from math import pi

r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

###################################################################
#Turn input values separated by comma into list and tuple

values = input("Input some comma seprated numbers : ")

list = values.split(",")
tuple = tuple(list)

print('List : ',list)
print('Tuple : ',tuple)

###################################################################
#Print documentation of built-in function(s)

print(abs.__doc__)

###################################################################
#Print calendar of the input year and month

import calendar

y = int(input("Input the year : "))
m = int(input("Input the month : "))

print(calendar.month(y, m))

###################################################################
#Diference of days between two dates

from datetime import date

f_date = date(2022, 3, 6)
l_date = date(2022, 5, 14)
delta = l_date - f_date

print(delta.days)

###################################################################
#Detect characters in a string

def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

print(is_vowel('c'))
print(is_vowel('e'))

###################################################################
#Check type of variable

thistuple = ("apple",)
print(type(thistuple))