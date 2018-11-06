"""This is a 
multiline docstring."""
# basic if condition
if 5 > 2:
  print("true")

# print range of charactors
b = "Hello, World!"
print(b[2:5])

# remote spaces from start and end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# get length of string
a = "Hello, World!"
print(len(a))

# do upper case
a = "Hello, World!"
print(a.upper())

# replace charactor
a = "Hello, World!"
print(a.replace("H", "J"))

# split string into array 
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# ask for input in cmd and print
print("Enter your name:")
x = input()
print("Hello, " + x)


