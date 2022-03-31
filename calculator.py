"""_____Question:
Input a and b taken from user. Perform a + b, a - b, a*b, a/b,
and store answers in different variables, and print
"""

print("Hello there! Let's do some math!\n")

while True:
	try:
		a = float(input("Enter the first number a (a<>0): "))
		while a == 0:
			print("a must not be equal to 0!")
			a = float(input("Enter the first number a (a<>0): "))
			
		b = float(input("Enter the second number b: "))

		print("""
Here are the math operations with a and b:
	a + b = {}
	a - b = {}
	a * b = {}
	a / b = {}
End of Program!
		""".format(a + b, a - b, a * b, a / b))
		break
	except:
		print("Error: Please enter numbers only!")
		continue