import sys
import math

# Print welcome
print('Welcome to the Circle Calculator!')

# Get the radius
r = input('Enter a radius: ')
try:
    r = int(r)
except ValueError:
    print("Numbers only")
    sys.exit()

# Find the area
area = math.pi * (r * r)
print('The area is', area)

# Find the permiter
perimeter = math.pi * (r * 2)
print('The perimeter is', perimeter)
