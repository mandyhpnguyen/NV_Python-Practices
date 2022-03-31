"""_____Question:
Find Areas and/or Perimeters of a chosen shape (square, rectangle, circle, triangle)
"""
print("Hello there! Let's find out areas and perimeters!\n")

# ------------------------- CIRCLE
def find_circle():
	while True:
		import math
		try:
			circle_radius = float(input("Enter the circle's radius: "))
			
			circle_area = math.pi * (circle_radius ** 2)
			circle_perimeter = 2 * math.pi * circle_radius
			
			print("""
	Your circle's radius is: {}
	Your circle's area is: {} square
	Your circle's circumference is: {}
			""".format(circle_radius, circle_area, circle_perimeter))
			break
		except:
			print("Error: Invalid Values! Please re-enter the number of circle's radius!")
			continue


# ------------------------- SQUARE
def find_square():
	while True:
		try:
			square_length = float(input("Enter the square's length: "))
			
			square_area = square_length ** 2
			square_perimeter = square_length * 4
			
			print("""
	Your square's length is: {}
	Your square's area is: {} square
	Your square's perimeter is: {}
			""".format(square_length, square_area, square_perimeter))
			break
		except:
			print("Error: Invalid Values! Please re-enter the number of square's length!")
			continue


# ------------------------- RECTANGLE
def find_rectangle():
	while True:
		try:
			rectangle_length = float(input("Enter the rectangle's length: "))
			rectangle_width = float(input("Enter the rectangle's width: "))
			
			rectangle_area = rectangle_length * rectangle_width
			rectangle_perimeter = (rectangle_length + rectangle_width) * 2
			
			print("""
	Your rectangle's length is: {}
	Your rectangle's width is: {}
	Your rectangle's area is: {} square
	Your rectangle's perimeter is: {}
			""".format(rectangle_length, rectangle_width, rectangle_area, rectangle_perimeter))
			break
		except:
			print("Error: Invalid Values! Please re-enter the numbers of rectangle's dimensions!")
			continue


# ----------------------- TRIANGLE
def find_triangle():
	while True:
		try:
			triangle_side_1 = float(input("Enter the triangle's first side: "))
			triangle_side_2 = float(input("Enter the triangle's second side: "))
			triangle_height = float(input("Enter the triangle's height: "))
			triangle_base = float(input("Enter the triangle's base: "))
			
			triangle_area = 0.5 * triangle_height * triangle_base
			triangle_perimeter = triangle_side_1 + triangle_side_2 + triangle_base
			
			print("""
	Your triangle's first side is: {}
	Your triangle's second side is: {}
	Your triangle's base is: {}
	Your triangle's height is: {}
	Your triangle's area is: {} square
	Your triangle's perimeter is: {}
			""".format(triangle_side_1, triangle_side_2, triangle_base, triangle_height, triangle_area,
			           triangle_perimeter))
			break
		except:
			print("Error: Invalid Values! Please re-enter the numbers of triangle's dimensions!")
			continue

while True:
	try:
		shape = int(input("""
Type the shape's number of your choice:
	(1) Circle
	(2) Triangle
	(3) Square
	(4) Rectangle
	
	"""))
		if 0 < shape <= 4:
			if shape == 1:
				print("You have chosen: Circle")
			elif shape == 2:
				print("You have chosen: Triangle")
			elif shape == 3:
				print("You have chosen: Square")
			else:
				print("You have chosen: Rectangle")
			# Improve by using dataframe later
		else:
			print("Error: Invalid value! You must enter a number from 1 to 4")
			continue
		break
	except:
		print("Error: Invalid value! You must enter a number from 1 to 4")
		continue

if shape == 1:
	find_circle()
elif shape == 2:
	find_triangle()
elif shape == 3:
	find_square()
else:
	find_rectangle()
	
print("End of Program!")