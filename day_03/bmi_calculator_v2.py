# 1st input: enter height in meters e.g: 1.65
height = float(1.75)
# 2nd input: enter weight in kilograms e.g: 72
weight = int(80)
# 🚨 Don't change the code above 👆

# 🚨 Expected output:
# "Your BMI is 18.28678, you are underweight."
# "Your BMI is 22.0, you have a normal weight."
# "Your BMI is 28.50752, you are slightly overweight."
# "Your BMI is 32.56189, you are obese."
# "Your BMI is 37.50000, you are clinically obese."

# Write your code below this line 👇
weight = int(weight)
height = float(height)
bmi = weight / (height * height)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")  # 18.28678,
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")  # 22.0,
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")  # 28.50752,
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")  # 32.56189,
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")  # 37.50000,
