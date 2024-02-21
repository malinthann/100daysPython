# Logical Operator
# and, or, not
a = 12
b = 10
c = 5
print(a > b and b > c)  # True
print(a > b and b < c)  # False
print(a < b and b > c)  # False
print(a < b and b < c)  # False
print(a > b or b > c)  # True
print(a > b or b < c)  # True
print(a < b or b > c)  # True
print(a < b or b < c)  # False
print(not a > b)  # False
print(not a < b)  # True
print(not a == b)  # True
print(not a != b)  # False
