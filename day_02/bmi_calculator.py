# 1st input: enter height in meters e.g: 1.65
height = 1.65
# 2nd input: enter weight in kilograms e.g: 72
weight = 72
# 🚨 Don't change the code above 👆

# 🚨 Expected output: 26

# Write your code below this line 👇
weight = int(weight)
height = float(height)
# Using the exponent operator **
BMI = weight / height ** 2
# or using multiplication and PEMDAS
BMI_2 = weight / (height * height)
print(int(BMI))
print(int(BMI_2))
