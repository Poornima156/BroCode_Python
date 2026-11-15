import math

# 1. Properly convert inputs from strings to floats
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))

# 2. Calculate the hypotenuse accurately
# math.hypot() is safer and more precise than manually doing (a**2 + b**2)**0.5
hypotenuse = math.hypot(side1, side2)

# 3. Print the result rounded to 2 decimal places properly
print(f"The hypotenuse of the triangle is: {hypotenuse:.2f}")