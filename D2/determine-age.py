"""_____Question:
- Take age from user
- Check age:
	+ if Age < 13 than User is a kid
	+ if Age >= 13 and Age <= 19 than User is a teen
	+ if Age > 19 than user is an Adult
"""
print("Hello there! Let's determine your age!\n")

user_name = input("What is your name?\n")
while True:
	try:
		age = int(input("What is your age?\n"))
		if age < 13:
			print("""
Hi {}! You are {}!
			""".format(user_name, "just a KID!"))
		elif 13 <= age <= 19:
			print("""
Hi {}! You are {}!
			""".format(user_name, "still a TEENAGER!"))
		else:
			print("""
Hi {}! You are {}!
			""".format(user_name, "an ADULT now!"))
		break
	except:
		print("Error: Not an integer number!!!")
		continue

print("End of Program!")