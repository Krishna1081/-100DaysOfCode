# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Convert weight and height into int and float
weight_conv = int(weight)
height_conv = float(height)

# Calculate BMI
BMI = weight_conv / (height_conv * height_conv)

# Print BMI
print(int(BMI))