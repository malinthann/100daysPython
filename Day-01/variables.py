# name is a variable that stores the input from the user.
# variables can used multiple times in this case name is used 3 times.

# variable name 1
name = input("What is your name? ")
print(name) # print out input

# variable name 2
name = "Thann"
print(name) # print out the string "Thann"

# variable name 3
name = "Lin"
print(name) # print out the string "Lin"

# variable name 4
name = input("What is your name? ")
# variable length 5
length = len(name) # count the length of the input string
print(length) # print out the length of the input string


a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print(b + a) # print out the value of b and a