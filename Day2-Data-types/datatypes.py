print("hello"[1]) #output is "e"  - this method is also called subscripting 
print("123") # out is "123"

#Integer
print(123 + 456) #output is 579 - it adds the number
print(123_234_345 + 456_980) #this is how large numbers are represented instead of ,

#Float
print(3.14159 + 5.666)

#Boolean 
a = 5
b = 2
print(bool(a < b)) #prints true or false

#Type conversion
num_char = len(input("What is your name?"))
print(type(num_char))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

a = 123_4
print(type(a))

print(str(10) + str(123))

#Executes in PEDMAS format P - Parentheses E - Exponent and also 
# the expression is checked from left to right. 
print (3 * 3 + 3 / 3 - 3) #prints 7
print (3 * ( 3 + 3 ) / 3 - 3) #prints 3

print(round(8 / 3,2))
print(round(8 / 3))

print(8 // 3)

score = 4 / 2
score /= 2 #similarly you can do += -= 
print(score) 

#using f-string
sc = 0
height = 1.5
isWin = True
print(f"you score is {sc} , height is {height}, winning is {isWin}")
