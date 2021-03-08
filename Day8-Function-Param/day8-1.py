import math

def paint(h,w,c):
    area = h * w 
    num_of_cans = math.ceil(area / c)
    print(f"The number of cans to be used is : {num_of_cans}")


height = int(input("Whats the height: "))
width = int(input("Whats the width : "))
cover = 5
paint(height,width,cover)