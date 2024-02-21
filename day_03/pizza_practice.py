print("Thank you for choosing Python Pizza Deliveries!")
size = "L"  # What size pizza do you want? S, M, or L
add_pepperoni = "Y"  # Do you want pepperoni? Y or N
extra_cheese = "N"  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# My code
bill = 0
if size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    else:
        bill += 0

if size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    else:
        bill += 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    else:
        bill += 0

if extra_cheese == "Y":
    bill += 1
else:
    bill += 0


final_bill = bill

print(f"Your final bill is: ${final_bill}.")


# Her code
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


pizza_size = input("What size pizza do you want? S, M, or L ")
if pizza_size == "S":
    bill += 15
    print(f"You choose (S) which is $15")
    wants_pepperoni = input("Do you want pepperoni? Y or N ")
    if wants_pepperoni == "Y":
        bill += 3
        print(f"You want Pepperoni which is $3")
    if wants_pepperoni == "N":
        bill += 0
        print(f"You don't want Pepperoni $0")
    wants_cheese = input("Do you want extra cheese? Y or N ")
    if wants_cheese == "Y":
        bill += 1
        print(f"You want Cheese which is $1")
    if wants_cheese == "N":
        bill += 0
        print(f"You don't want Cheese which is $0")

if pizza_size == "M":
    bill += 20
    print("You choose (M) which is $20")
    wants_pepperoni = input("Do you want pepperoni? Y or N ")
    if wants_pepperoni == "Y":
        bill += 3
        print(f"You want Pepperoni which is $3")
    if wants_pepperoni == "N":
        bill += 0
        print(f"You don't want Pepperoni $0")
    wants_cheese = input("Do you want extra cheese? Y or N ")
    if wants_cheese == "Y":
        bill += 1
        print(f"You want Cheese which is $1")
    if wants_cheese == "N":
        bill += 0
        print(f"You don't want Cheese which is $0")

if pizza_size == "L":
    bill += 25
    print("You choose (M) which is $25")
    wants_pepperoni = input("Do you want pepperoni? Y or N ")
    if wants_pepperoni == "Y":
        bill += 3
        print(f"You want Pepperoni which is $3")
    if wants_pepperoni == "N":
        bill += 0
        print(f"You don't want Pepperoni $0")
    wants_cheese = input("Do you want extra cheese? Y or N ")
    if wants_cheese == "Y":
        bill += 1
        print(f"You want Cheese which is $1")
    if wants_cheese == "N":
        bill += 0
        print(f"You don't want Cheese which is $0")

final_price = bill
print(f"Your final bill is: ${final_price}.")
