# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1 + name2
print(names.lower())
t = names.lower().count("t")
r = names.lower().count("r")
u = names.lower().count("u")
e = names.lower().count("e")
score_1 = t + r + u + e


l = names.lower().count("l")
o = names.lower().count("o")
v = names.lower().count("v")
e = names.lower().count("e")
score_2 = l + o + v + e

total_score = score_1 + score_2

if (total_score < 10) or (total_score > 90):
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (total_score >= 40) and (total_score <= 50):
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}.")