states_india = [
                "Tamil Nadu",
                "Kerala",
                "Karnataka",
                "Andhra Pradesh",
                "Maharashtra"    ]

states_india[0] = "Tamilnadu" #A particular item of list can be overwritten this way

states_india.append("Orissa") #Adding an item to the end of the list

num = int(input("Enter number between 0 and 5 :"))
print(states_india[num]) 
print(len(states_india))