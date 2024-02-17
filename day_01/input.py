# input() function is used to take input from the user
input("Hello, what is your name?")

# input() can be used in print() function
# input will show first and then the print function will execute.
print("Hello, " + input("What is your name?") + "!") 

name1 = input("What is your name? ")
print(name1) #This line will print the text and line 1 of the input into the output.
name2 = input()
print(name2) #This line will only print the name on line 2 of the input pane.
name3 = input()
print(name3)

# count string length using len() function
name = "Jane"
print(len(name)) # This will print the length of the string "Jane" which is 4.

# count the length of the input string
print(len(input("What is your name? ")))

num_1 = 5
num_2 = 7
result = num_1 + num_2

#use f-string to print the result
print(f"The result is {num_1} + {num_2} = {result}")
