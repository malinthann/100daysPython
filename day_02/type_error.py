num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.") # error num_char is an integer and cannot be concatenated with a string
# print(type (num_char)) # <class 'int'>
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.") # This will print the number of characters in the input name.

a = float(123)
print(type(a)) # <class 'float'>

print(70 + float("100.5")) # 170.5

print(str(70) + str(100)) # 70100