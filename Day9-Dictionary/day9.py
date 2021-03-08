programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again"
}


# Retrieving items for dictionary
print(programming_dictionary["Function"])

# Adding new items to dictionary
programming_dictionary["Execute"] = "The action of seeing the outcome"
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in the dictionary
programming_dictionary["Bug"] = "An error that needs to be rectified"

print(programming_dictionary)

#Loop through a dictionary   : This code just gives you the key
for thing in programming_dictionary:
    print(thing)

for key in programming_dictionary:
    print(key, programming_dictionary[key])