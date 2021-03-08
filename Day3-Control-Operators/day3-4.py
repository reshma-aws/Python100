#Multiple IF statement
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age? :"))
  if age < 12:
    print("Child ticket is $5")
    bill = 5
  elif age <=18:
    print("Youth ticket is $7")
    bill = 7
  else: 
    print("Adult ticket is $12")
    bill = 12
  photo = input("Do you want a photo taken? Y / N : ")
  if photo == "Y" or photo =='y':
      bill += 3
  print(f"your final bill is $ {bill}")

else:
  print("You cannot ride the rollercoaster")