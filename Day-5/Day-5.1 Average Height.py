# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for j in range(len(student_heights)):
    student_heights[j] = int(student_heights[j])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
average = 0
for i in range(len(student_heights)):
    average += int(student_heights[i])
average = round(average/len(student_heights))
print(average)