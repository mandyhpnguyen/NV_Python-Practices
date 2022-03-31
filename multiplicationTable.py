""" Question:
- Take a number from user's input
- Print its multiplication of itself with 1 - 10
"""
print("Hi there! Let's find the multiplication table of a number!")
multiplier = float(input("Enter a number to multiple: "))
i = 1
while i <= 10:
    print("{} x {} = {}".format(multiplier, i, multiplier * i))
    i += 1
    
print("End of Program!")