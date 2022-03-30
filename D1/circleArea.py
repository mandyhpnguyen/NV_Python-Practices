import math

name = input("What's your name?\n")
print("Hello,", name, "I will give you area of circle!")

# Find the area of circle with given radius
radius_input = input("Enter the radius?\n")

#print(radius_input.isnumeric())

try:
	radius = float(radius_input)
	print("Your circle's area is:", math.pow(radius, 2)*math.pi)
except:
	print("Error: Please provide a number!!")