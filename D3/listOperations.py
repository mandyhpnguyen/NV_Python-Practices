# Create a list of [1, 2, 3, 4]
lst = [i for i in range(1, 5)]
print(lst)

# Insert "05" to list
lst.insert(4, 5); print(lst)

# Insert "110" to list
lst.insert(5, 110); print(lst)

# Insert "06" to list
lst.insert(6, 6); print(lst)

# Insert "25" to list
lst.insert(7, 25); print(lst)

# Remove "06" from list
lst.remove(6); print(lst)

# Append "09" to list
lst.append(9); print(lst)

# Append "01" to list
lst.append(1); print(lst)

# Reverse the elements of the list
lst.reverse(); print(lst)

# Count "05" in list
lst.count(5)

# Find index of "01"
lst.index(1)

# Pop the last item
lst.pop(); print(lst)

# Extend [200, 100]
lst.extend([200, 100]); print(lst)

# Copy to a new list
new_lst = lst.copy()

# Sort list ascending-ly and descending-ly
new_lst.sort()
new_lst.sort(reverse=True)