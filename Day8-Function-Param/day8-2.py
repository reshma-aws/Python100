
def prime(number):
    is_prime = True
    for i in range (2, number): #To check is the number is divisible by anything less than itself. Eg if number = 7, check if 7 is divisible from ( 2, 3, 4,5,6)
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime number")
    else:
        print("Not a Prime Number")


number = int(input('Enter a number to check: '))
prime(number)