print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = percent / 100
tip_amt = bill + tip 
total_bill = bill + tip_amt
per_person = total_bill / people
final_amt = round(per_person,2)

# bill = input("What was the total bill? $")
# percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
# people = input("How many people to split the bill? ")

# total_bill = float(bill) + (float(bill) + int(percent)/100)
# share = total_bill / int(people)
# share = "{:2f}.format(total_bill)"
# print(f"${share}"")

print(f"Each person should pay ${final_amt}")
