# Alissa Sheikh 1623952
import math

# Prompt the user to input a wall's height and width. Calculate and output the wall's area
height = float(input('Enter wall height (feet):\n'))
width = float(input('Enter wall width (feet):\n'))
area = height * width
# Use a math function to round up to the nearest gallon.
print('Wall area: ' + str(int(round(area))) + ' square feet')
# Extend to also calculate and output the amount of paint in gallons needed to paint the wall (floating point)
paint_needed = area / 350  # area/ one gallon of paint
paint_gallons = int(math.ceil(paint_needed))
print('Paint needed: %.2f gallons' % paint_needed)
# number of cans needed
print('Cans needed: ' + str(paint_gallons) + ' can(s)\n')
# Extend by prompting the user for a color they want to paint the walls. Calculate/output the total cost depending
color = input('Choose a color to paint the wall:\n')
if color == "red":
    cost = 35 * paint_gallons
elif color == "blue":
    cost = 25 * paint_gallons
elif color == "green":
    cost = 23 * paint_gallons
else:
    cost = 0
print('Cost of purchasing ' + color + ' paint: $' + str(cost))
