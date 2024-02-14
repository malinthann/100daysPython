# input() function is used to take input from the user
input("Hello, what is your name?")

# input() can be used in print() function
print("Hello, " + input("What is your name?") + "!")

name1 = input()
name2 = input()
name3 = input()

name1 = input("What is your name? ")
print(name1) #This line will print the text and line 1 of the input into the output.
name2 = input()
print(name2) #This line will only print the name on line 2 of the input pane.
name3 = input()
print(name3)

num_1 = 5

num_2 = 7

result = num_1 + num_2

#use f-string to print the result
print(f"The result is {num_1} + {num_2} = {result}")