import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)  # Corrected line

print(f"{names[random_choice]} is going to buy the meal today!")
