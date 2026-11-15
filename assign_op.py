import math
from math import ceil


x=3.14
y=-2
z=2.5
r1 = [x, y, z]
print(r1)
print("Rounding r1:")  # rounding means to round the number to the nearest integer and if the number is exactly halfway between two integers, it rounds to the nearest even integer for example, 2.5 rounds to 2 and 3.2 rounds to 4
for i in range(3):
    print(round(r1[i]))
print("Absolute values of r1:") #absolute value means to remove the negative sign from a number
for i in range(3):
    print(abs(r1[i]))
print("Ceiling of r1:") #ceiling means to round the number up to the nearest integer
for i in range(3):
    print(ceil(r1[i])) 
print("Floor of r1:") #floor means to round the number down to the nearest integer
for i in range(3):
    print(int(r1[i]))
print("maximum of r1:", max(r1)) #maximum means to find the largest number in a list
print("minimum of r1:", min(r1)) #minimum means to find the smallest number in a list
print("Sum of r1:", sum(r1)) #sum means to add all the numbers in a list
print("Length of r1:", len(r1)) #length means to find the number of elements in a list
print("Sorted r1:", sorted(r1)) #sorted means to arrange the numbers in ascending order
print("Reversed r1:", list(reversed(r1))) #reversed means to arrange the numbers in descending orderpr