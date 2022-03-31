""" _____Question: Triangle Pattern 1
- T
"""


# (b) Top-left Right Angle
def draw_triangle_topLeft_rightAngle(lineCount, trianglePattern):
	for i in range(lineCount, 0, -1):
		for j in range(i):
			print(trianglePattern, end="")
		print("")


# (a) Top-right Right Angle
def draw_triangle_topRight_rightAngle(lineCount, trianglePattern):
	for i in range(1, lineCount + 1):
		for j in range(i):
			print(" ", end="")
		for j in range(lineCount + 1 - i):
			print(trianglePattern, end="")
		print("")


# (d) Bottom-left Right Angle
def draw_triangle_bottomLeft_rightAngle(lineCount, trianglePattern):
	for i in range(1, lineCount + 1):
		for j in range(i):
			print(trianglePattern, end="")
		print("")


# (c) Bottom-right Right Angle
def draw_triangle_bottomRight_rightAngle(lineCount, trianglePattern):
	for i in range(1, lineCount + 1):
		for j in range(lineCount - i):
			print(" ", end="")
		for j in range(i):
			print(trianglePattern, end="")
		print("")


# (e) Equal Triangle
def draw_triangle_equalSides(lineCount, trianglePattern):
	for i in range(1, lineCount + 1):
		for j in range(lineCount - i):
			print(end=" ")
		for j in range(i):
			print("{} ".format(trianglePattern), end="")
		print(" ")


while True:
	
	n = int(input("Enter the Number of Lines of the Triangle: "))
	pattern = input("Enter the Pattern of Triangle: ")
	
	while True:
		triangleIndex = str(input("""
Choose one letter for the triangle of your choice:

(a) Top-Right Right Angle Triangle
(b) Top-Left Right Angle Triangle
(c) Bottom-Right Right Angle Triangle
(d) Bottom-Left Right Angle Triangle
(e) Equal Sides Triangle (Isosceles)

OR

Type "all" if you want to print all 5 triangles.

Your answer is:	"""))
		if triangleIndex.lower() == "a":
			draw_triangle_topRight_rightAngle(n, pattern)
			break
		elif triangleIndex.lower() == "b":
			draw_triangle_topLeft_rightAngle(n, pattern)
			break
		elif triangleIndex.lower() == "c":
			draw_triangle_bottomRight_rightAngle(n, pattern)
			break
		elif triangleIndex.lower() == "d":
			draw_triangle_bottomLeft_rightAngle(n, pattern)
			break
		elif triangleIndex.lower() == "e":
			draw_triangle_equalSides(n, pattern)
			break
		elif triangleIndex.lower() == "all":
			draw_triangle_topRight_rightAngle(n, pattern)
			draw_triangle_topLeft_rightAngle(n, pattern)
			draw_triangle_bottomRight_rightAngle(n, pattern)
			draw_triangle_bottomLeft_rightAngle(n, pattern)
			draw_triangle_equalSides(n, pattern)
			break
		else:
			print("Error: Invalid Letter!!! Please re-enter a, b, c, d or all only!")
			continue
		break
	
	while True:
		exit_prompt = input("Would you to continue? (Type: \"yes\"/\"no\") ")
		if exit_prompt.lower() == "yes" or exit_prompt.lower() == "no":
			break
		else:
			print("Please enter \"yes\" or \"no\" only!")
			continue
	
	if exit_prompt.lower() == "yes":
		continue
	else:
		print("\nEnd of Program!\n")
		break