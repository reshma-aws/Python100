# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆

total_height = 0
num = 0
for height in student_heights:
  total_height += height
  num += 1
print(total_height)
print(num)

print("Average height of students is : ", round((total_height/num),2)) 
#Write your code below this row 👇




