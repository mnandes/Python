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

###################################################################
#Manipulating strings

a = "hello world"

#Length of String
len(a)

#Returns the number of l's in the string
a.count('l')

#Finds the word or character in the string
a.find('h')

#Finds the letters in the string
a.index('h')

#Split by whitespace. Returns a list of all the splits
a.split(' ')

#Starts or ends with 'h' or 'o'
a.startswith('h')
a.endswith('o')

#Print a 10 times
print(a * 10)

#Replace words in a string
a.replace("hello", "world")

#Capitalize Every Letter
a.upper()

#Lower Case Every Letter
a.lower()

#Capitalize First Letter of Every Word (Uses whitespace to distinguish separate words)
a.title()

#Capitalize First Letter
a.capitalize()

#Swap Lower Case with Upper Case and Upper Case with Lower Case
a.swapcase()

#Reverse String
reversed(a)

#Removes Leading and Trailing Characters
a.strip()

#Removes Leading Characters
a.lstrip()

#Removes Trailing Characters
a.rstrip()

#Concatenate strings
a + "!!"

#Check if all char are alphanumeric 
a.isalnum()

#Check if all char in the string are alphabetic
a.isalpha() 

#Test if string contains digits
a.isdigit() 

#Test if string contains title words
a.istitle() 

#Test if string contains upper case
a.isupper() 

#Test if string contains lower case
a.islower() 

#Test if string contains spaces
a.isspace() 

#Add a whitespace between every char in the string
" ".join(a)

#Second Character
print(a[1]) 

#Last Character
print(a[-1])

#Last 3 Characters
print(a[-3 :])

#Get all but the 3 last Characters
print(a[: -3])

#Get all but the 3 first Characters
print(a[3 :])

#Second to Last Character (Not Including the Last)
print(a[1 : -1])


###################################################################
#For Loops (While loops work the same)


#Loop through array
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for index in range(len(fruits)):
    print(fruits[index])

#Loop through string characters
for x in "banana":
  print(x)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")  
d = dict()
d['xyz'] = 123
d['abc'] = 345

for i in d :
    print("%s  %d" %(i, d[i]))

#Iterating over a set
print("\nSet Iteration")
set1 = {1,2,3,4,5,6}

for i in set1:
    print(i),

#For loop keywords

    #skip to next iteration of the loop
    #continue

    #exit the loop
	#break

    #executes this branch of code in case loop succeeds normally, without “breaking”
	#else

#Loop through range of numbers

#Loop from 0 to 6
for x in range(6):
    print(x)

#Loop from 2 to 6
for x in range(2,6):
  print(x)

#Loop from 2 to 30 in increments of 3
for x in range(2, 30, 3):
  print(x)

#Decrementing for loop (1st argument > 2nd argument and 3rd argument negative)
for x in range(6, 2, -1):
  print(x)

#Empty for loop, pass prevents getting an error
for x in [0, 1, 2]:
  pass

###################################################################
#Swapping 2 variables in 1 line

x, y = y, x

###################################################################
#Get execution times

import time

def inRange():
    start_time = time.time()
    #Insert testing code
    print("InRange--- %s seconds ---" % (time.time() - start_time))


###################################################################
#Data Types and Structures

#Numbers
#Int
integer = 100

#Float
floating_point = 100.0

#Long
#Complex

#String
string = "Nandes"

#Multiple Assignment
integer, floating_point, string = 100, 100.0, "Nandes"

#Lists
li = [1,2,3] #String manipulations such as string[2:4] also work on tuples

#Tuples
tuple = (123, '123', 'Nandes') #String manipulations such as string[2:4] also work on tuples

tuple[2] = 1000    # Invalid syntax with tuple due to it being immutable

#Dictionary
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(dict['one'])       # Prints value for 'one' key
print(dict[2])           # Prints value for 2 key
print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values()) # Prints all the values

#Data Type Conversions
s = "string"
x = 1
base = 1

int(x) #Converts x to an integer. base specifies the base if x is a string.
float(x) #Converts x to a floating-point number.
complex(x) #Creates a complex number.

str(x) #Converts object x to a string representation.
repr(s) #Converts object x to an expression string.
eval(s) #Evaluates a string and returns an object.

tuple(s) #Converts s to a tuple.
list(s) #Converts s to a list.
set(s) #Converts s to a set.
dict(d) #Creates a dictionary. d must be a sequence of (key,value) tuples.
frozenset(s) #Converts s to a frozen set.

chr(x) #Converts an integer to a character.
ord(x) #Converts a single character to its integer value.

hex(x) #Converts an integer to a hexadecimal string.
oct(x) #Converts an integer to an octal string.

#Using lists as stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
[3, 4, 5, 6, 7]
stack.pop()
7
stack
[3, 4, 5, 6]
stack.pop()
6
stack.pop()
5
stack
[3, 4]

#Using lists as queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
'Eric'
queue.popleft()                 # The second to arrive now leaves
'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

#Creating and populating lists with values
squares = list(map(lambda x: x**2, range(10))) #is the same as
squares = [x**2 for x in range(10)]