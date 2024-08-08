#https://www.w3schools.com/python/default.asp
#https://youtu.be/1mLmW0sTzjw?si=I-t5yQoqDAAWR1sk--1hr done
#tomorrow-day2-https://www.w3schools.com/python/python_casting.asp
"""
1.Python Tutorial-Home
2.Python Introduction
3.Python Getting Started
4.Python Syntax
5.Python Comments
6.Python Variables
7.Python Data Types
8.Python Numbers
"""

print('hello world')
print("again hello world")
print('''abar again hello world''')

#print(''''abar again hello world'''')
#SyntaxError: unterminated string literal (detected at line 4)

"""
multi line comment--xyz
"""
print('hello world after multi line comment')

"""
module?:is a package--as like a readymate burger--foodpanda burger
PIP?:is a package manager--as like a burger carrier--foodpanda delivery man

module 2 types:
1.built-in-module
2.user defined module(external module)
"""
#python built in modlue?:https://docs.python.org/3/py-modindex.html
#python external modlue?:https://www.geeksforgeeks.org/external-modules-in-python/
#https://www.w3schools.com/python/python_modules.asp

name = "sohel"
print(name)

#1.Python Tutorial-Home

"""
Python is a popular programming language.
Python can be used on a server to create web applications.
"""
print('hello world')
if 5 > 2:
    print("YES")

#2.Python Introduction

"""
What is Python?

Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

    web development (server-side),
    software development,
    mathematics,
    system scripting.

"""

"""
What can Python do?

    Python can be used on a server to create web applications.
    Python can be used alongside software to create workflows.
    Python can connect to database systems. It can also read and modify files.
    Python can be used to handle big data and perform complex mathematics.
    Python can be used for rapid prototyping, or for production-ready software development.
"""

"""
Why Python?

    Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
    Python has a simple syntax similar to the English language.
    Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
    Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
    Python can be treated in a procedural way, an object-oriented way or a functional way.
"""

"""
Python Syntax compared to other programming languages

    Python was designed for readability, and has some similarities to the English language with influence from mathematics.
    Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
    Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose
"""

print("Hello, World!")


#3.Python Getting Started
#to check python installed or not : C:\Users\Your Name>python --version 
#The way to run a python file is like this on the command line:
#C:\Users\Your Name>python helloworld.py 
print("Hello, World!")

#PS D:\py\day-1-python-w3> python day1.py 



#4.Python Syntax

"""
Python Indentation

Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.
"""
if 5 > 2:
  print("Five is greater than two!")

#Python will give you an error if you skip the indentation:
"""
if 5 > 2:
print("Five is greater than two!")

 File "demo_indentation_test.py", line 127
    print("Five is greater than two!")
        ^
IndentationError: expected an indented block 
"""

#The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

if 5 > 2:
 print("Five is greater than two!")  
if 5 > 2:
        print("Five is greater than two!") 

#You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

if 5 > 2:
 print("Five is greater than two!") 
 print("Five is greater than two!")

"""
 if 5 > 2:
 print("Five is greater than two!") 
        print("Five is greater than two!")
 
  File "demo_indentation2_error.py", line 149
    print("Five is greater than two!")
    ^
IndentationError: unexpected indent 
"""

x = 5
y = "Hello, World!"

print(x)
print(y)


#5.Python Comments

#Comments starts with a #, and Python will ignore them:
#This is a comment.
print("Hello, World!")

#Comments can be placed at the end of a line, and Python will ignore the rest of the line:
print("Hello, World!") #This is a comment.

#print("Hello, World!")
print("Cheers, Mate!")


"""
This is a comment
written in
more than just one line
"""
print("Hello, World!") 


#6.Python Variables
x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4
x = "Sally"
print(x)

#Casting

#If you want to specify the data type of a variable, this can be done with casting.

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

x = 5
y = "John"
print(type(x))
print(type(y))

#Single or Double Quotes?

#String variables can be declared either by using single or double quotes:

x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)


#Case-Sensitive

#Variable names are case-sensitive.

a = 4
A = "Sally"

print(a)
print(A)

"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#Pascal Case

#Each word starts with a capital letter:
MyVariableName = "Johnnny"
print(MyVariableName)

#Snake Case

#Each word is separated by an underscore character:
my_variable_name = "John"
print(my_variable_name)

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

x = y = z = "Orange"

print(x)
print(y)
print(z)

#Unpack a Collection

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x,y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z +" enJoy Python")

x = 5
y = 10
print(x + y)
print(x,y)

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x = 5
y = "John"
print(x, y)
"""
print(x+y)
Traceback (most recent call last):
  File "d:\py\day-1-python-w3\day1.py", line 323, in <module>
    print(x+y)
          ~^~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

#Global Variables

"""
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""
#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x+" enJoy python")

myfunc()


"""
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
"""

x = "awesomeeeee"

def myfunc():
  x = "fantasticccc"
  print("Python is " + x)

myfunc()

print("Python is " + x)


"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

"""

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

def myfunc():
  global x  
  x= "fantasticcccccccccccccccc"
  print("Python is " + x)

myfunc()
print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x,y,z = "Orange", "Banana", "Cherry"
print(x,y,z)

x = y = z = "Orange"
print(x,y,z)


#7.Python Data Types

"""
Python has the following data types built-in by default, in these categories:
Text Type:  	str
Numeric Types: 	int, float, complex
Sequence Types: list, tuple, range

Mapping Type: 	dict
Set Types: 	    set, frozenset

Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	    NoneType
"""

x = 5
print(type(x)) 

x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = 20.5
print(x)
print(type(x)) 


x = 5+2j

#display x:
print(x)
print(type(x)) 


x = ["apple", "banana", "cherry"]

print(x)
print(type(x)) 


x = ("apple", "banana", "cherry")
print(x)
print(type(x)) 

x = range(16)
print(x)
print(type(x)) 

x = {
   "name" : "John", 
   "age" : 36
   }

#display x:
print(x)
print(type(x)) 


x = {"apple", "banana", "cherry"}
print(x)
print(type(x)) 


x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) 

x = ({"appleee", "bananaaaa", "cherryyy"})
print(x)
print(type(x)) 


x = True
x = False
print(x)
print(type(x))


x = b"Hello"
print(x)
print(type(x)) 


x = bytearray(7)
print(x)
print(type(x)) 

x = memoryview(bytes(5))
print(x)
print(type(x)) 

x = memoryview(bytes(7))
print(x)
print(type(x)) 

print(x)
print(type(x)) 

x = None

#display x:
print(x)
print(type(x)) 



x = str("Hello World")

#display x:
print(x)
print(type(x)) 


x = int(20)

#display x:
print(x)
print(type(x)) 

x = float(20)

#display x:
print(x)
print(type(x)) 



x = float(20.5)

#display x:
print(x)
print(type(x)) 


x = complex(10+1j)

#display x:
print(x)
print(type(x)) 


x = list(("apple", "banana", "cherry"))

#display x:
print(x)
print(type(x)) 


x = tuple(("apple", "banana", "cherry"))

#display x:
print(x)
print(type(x)) 


x = range(60)

#display x:
print(x)
print(type(x))


x = dict(name="John", age=36)

#display x:
print(x)
print(type(x))


x = set(("apple", "banana", "cherry"))

#display x:
print(x)
print(type(x)) 


x = frozenset(("apple", "banana", "cherry"))

#display x:
print(x)
print(type(x))


x = bool(5)

#display x:
print(x)
print(type(x))

x = bool(-5)

#display x:
print(x)
print(type(x))

x = bool(0)

#display x:
print(x)
print(type(x))

x = bytes(5)

#display x:
print(x)
print(type(x)) 


x = bytearray(5)
print(x)
print(type(x)) 


x = memoryview(bytes(5))
print(x)
print(type(x)) 

x = ("apple", "banana", "cherry")
print(x)
print(type(x))



###8.Python Numbers###
"""
There are three numeric types in Python:

    int
    float
    complex

"""

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(x)
print(y)
print(z)


print(type(x))
print(type(y))
print(type(z))


x = 1.10
y = 1.0
z = -35.59
print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


x = 35e3
y = 12E4
z = -87.7e100
print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


x = 3+5j
y = 5j
z = -5j
print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


#Type Conversion

#You can convert from one type to another with the int(), float(), and complex() methods:

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


#Note: You cannot convert complex numbers into another number type.

"""
Random Number

Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
"""

import random

print(random.randrange(1, 10))


x = 5
x = complex (x)
print(x)
print(type(x))