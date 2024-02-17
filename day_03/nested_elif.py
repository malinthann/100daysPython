# # Nested if/else statement
# print("Welcome to the rollercoaster!")
# height = float(input("Enter your height in cm: "))

# if height >= 120:
#     print("You can ride the rollercoaster!")  # True
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5.")  # True
#     else:
#         print("Please pay $7.")  # False
# else:
#     print("Sorry, you have to grow taller before you can ride.")  # False

# if / elif / else statement
print("Welcome to the rollercoaster!")
height = float(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster!")  # True
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")  # True
    else:
        print("Please pay $12.")  # False
else:
    print("Sorry, you have to grow taller before you can ride.")  # False

# So in this game if you height are greater than 120 cm you can ride,
# but if you are less than 120 cm you can't ride.
# If you are less than 12 years old you pay $5.
# If you are less than 18 or equal 18 years old you pay $7.
# If you are 18 years old or older you pay $12.

print("Welcome to the rollercoaster!")
height = float(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster!")  # True
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif age < 22:
        print("Please pay $10.")
    elif age <= 65:
        print("Please pay $12.")
    else:
        print("Please pay $14.")
else:
    print("Sorry, you have to grow taller before you can ride.")  # False
