"""_____Question:
- Take user's input
- Key is the name of superhero
- Values is his/her alliance to the superhero team
"""
import sys

print("Hi there! Let's save some heroes' identities!")
while True:
	try:
		hero_count = int(input("Enter the numbers of hero to save in dictionary: "))
		if hero_count == "exit.":
			sys.exit()
		break
		# =====================
	except:
		print("Error: Invalid values! Please enter an integer number!")
		continue

hero_list = {}
i = 1
for i in range(hero_count):
	hero_name = input("Enter hero's NAME: ")
	# Exit code ===========
	if hero_name == "exit.":
		sys.exit()
	# =====================
	hero_alliance = input("Enter hero's ALLIANCE: ")
	# Exit code ===========
	if hero_alliance == "exit.":
		sys.exit()
	# =====================
	hero_list[hero_name] = hero_alliance
	i = i + 1

print("\n", hero_list, "\n")
print("""
List of Heroes and Alliances:

{:<13} {:<10}""".format("HERO", "ALLIANCE"))
for key, value in hero_list.items():
	hero_name = key
	hero_alliance = value
	print("{:<13} {:<10}".format(hero_name, hero_alliance))
print("\nEnd of Program!")