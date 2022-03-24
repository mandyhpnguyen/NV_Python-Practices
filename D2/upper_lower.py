"""_____Question
- Check if user's input is in LOWER or UPPER case and print the answer
- Return the 2 new string with ONE in LOWER case and ONE in UPPER case
"""
print("Hi there! Let's check Lower/Upper case of your string!")

while True:
	user_str = input("Let's type some words: ")
	try:
		if float(user_str).is_integer():
			print("Error: You just entered an INTEGER number!")
		else:
			print("Error: You just entered an DECIMAL number!")
		print("Please re-enter a word or phrase!")
		continue
	except:
		if user_str.islower():
			print("You have entered character(s) in lower case!")
			print("""
Here is input in:
	- Lower case: {}
	- Upper case: {}
			""".format(user_str.lower(), user_str.upper()))
		elif user_str.isupper():
			print("You have entered character(s) in upper case!")
			print("""
Here is input in:
	- Lower case: {}
	- Upper case: {}
			""".format(user_str.lower(), user_str.upper()))
		else:
			print("You have entered character(s) in both lower and upper case! ")
			print("""
Here is input in:
	- Lower case: {}
	- Upper case: {}
			""".format(user_str.lower(), user_str.upper()))
	
	# Check if user wants to continue checking lower/upper case:
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
		print("End of Program!")
		break