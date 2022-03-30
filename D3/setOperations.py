"""_____Question:
- User input 2 list of names
- Perform operations:
	+ Combine all the item in 2 list, but do not repeat items
	+ Find items in 2 list, but do
	+ Find the items which are in list 1 but not in list 2
	+ Find the items which are not common in both list
- Input list 1: Sai Gon, Viet Nam, US, Mandy, Nani, India, Delhi, Nana, Phuong
- Input list 2: US, Canada, Sai Gon, Delhi, India
"""
# Take User's input of 2 lists of names
lst1 = list(map(str, input("Enter the first list of names seperated by commas: ").split(", "))); print(
		lst1, "\n")
lst2 = list(map(str, input("Enter the second list of names separated by commas: ").split(", "))); print(
		lst2, "\n")

# Convert to sets
set1 = set(lst1); print(set1)
set2 = set(lst2); print(set2)

# Combine unique items
unionSet = set1 | set2
print("\nThe items in the combined list:\n", unionSet, "\n")

# Find common items
intersectSet = set1 & set2
print("The common items appear in both sets are:\n", intersectSet, "\n")

# Find unique items only in set 1 but not in set 2
subtractSet = set1 - set2
print("The unique items only in set 1 but not in set 2 are:\n", subtractSet, "\n")

# Find the items which are not common in both list
exOrSet = set1^set2
print("The items that are not common in both list:\n", exOrSet)