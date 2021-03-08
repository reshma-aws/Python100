# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height * height)
final_bmi = round(bmi,2)
if final_bmi < 18.5:
  print("You are underweight")
elif final_bmi >=18.5 and final_bmi < 25:
  print("You have a normal weight")
elif final_bmi >= 25 and final_bmi < 30:
  print("You are overweight")
elif final_bmi >= 30 and final_bmi < 35:
  print("You are obese")
else:
  print("You are clinically obese")


