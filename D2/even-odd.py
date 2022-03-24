"""______Question
Check whether the input is even or odd
"""
print("Hello there! Let's find even and odd numbers!\n")

while True:
	try:
		number = int(input("Enter an integer: "))
		if number % 2 == 0:
			print("{} is an even number!".format(number))
		else:
			print("{} is an odd number!".format(number))
		break
	except:
		print("Error: Invalid Values! Your input must be an integer number!")
		continue

print("End of Program!")