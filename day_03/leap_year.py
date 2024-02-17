# Which year do you want to check?
year = int(1776)
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Case 1 : Output | Leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
