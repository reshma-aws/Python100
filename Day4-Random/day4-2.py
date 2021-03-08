# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_of_names = len(names)

ran_num = random.randint(0, num_of_names - 1)

# ran_choice = random.choice(names) # This is a simpler way to choose from list

print("Person who will pay is : ", names[ran_num])