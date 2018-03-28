"""
Prog:   rectCalc.py
Name:   Student Name
Date:   12/03/18
Desc:   Calculates the area and perimeter of a rectangle.
"""

import sys

# Display welcome message.
print('Welcome to the Rectangle Calculator!')

# Use input to get the rectangle's length and width (2 lines).
# - Remember to provide a prompt message for each input.
length = input("Enter length: ")
width = input("Enter width: ")


# Convert length and width to integers.
try:
    length = int(length)
    width = int(width)
except ValueError:
    print("Numbers only")
    sys.exit()

# Calculate the area (1 line: length times width).
area = length * width

# Display the area.
print('The area is', area)

# Calculate and display the perimeter (2 lines: P = 2*length + 2*width).
perimeter = (2 * length) + (2 * width)
print("The perimeter is: {}".format(perimeter))
