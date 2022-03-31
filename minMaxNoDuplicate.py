"""_____Question: Remove duplicate, find largest and smallest item from list
- Take list of numbers as user's input
- Remove duplicates
- Find the smallest number
- Find the largest number
"""
# NOTE: This script cannot handle 4 and 4.0
import math

print("Hi there! Let's do some cleanings!")
# "Mandy", "mandy", "Nidhi", "nidhi", "mandy", "nidhi"
# 0, 2, 4, 5.3, 6, 2, 3, 4
# 4, 4, 3.5, 39, Mandy, 84, Nidhi

# ---------------------Get Input
while True:
	inputList = list(map(str, input("Enter list of numbers separated with \", \":\n").split(", ")))
	i = 0
	passList = []
	failList = []
	for i in range(len(inputList)):
		try:
			if type(float(inputList[i])) == float:
				passList.append(inputList[i])
				continue
		except:
			failList.append(inputList[i])
			continue
		i = i + 1

	if len(failList) != 0:
		print("""
Error: You have entered strings instead of numbers!
Your List: {}
Numbers in your list: {}
Strings in your list: {}
""".format(", ".join(inputList), ", ".join(passList), ", ".join(failList)))
		continue
	else:
		print("Your Original List:")
		print(", ".join(inputList))
		break

# ---------------------Remove Duplicate
numberSet = set(inputList)
print("Your Number List without Duplicates:")
print(", ".join(str(x) for x in numberSet))

# ---------------------Min-Max of Set
print("The Largest Number is:", max(numberSet))
print("The Largest Number is:", min(numberSet))

print("End of Program!")