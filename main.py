# Alissa Sheikh 1623952

# present: Enter amount of lemon juice (in cups):
lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))

# present: Enter amount of water (in cups):
water = float(input('Enter amount of water (in cups):\n'))

# present:Enter amount of agave nectar (in cups):
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))

# present : How many servings does this make?
servings = int(input('How many servings does this make?\n'))

# present: Lemonade ingredients - yields X.00 servings X.00 cup(s) lemon juice
print()
print(f'Lemonade ingredients - yields {servings:.2f} servings')

# X.00 cup(s) lemon juice
print(f'{lemon_juice:.2f} cup(s) lemon juice')

# X.00 cup(s) water
print(f'{water:.2f} cup(s) water')

# X.00 cup(s) agave nectar
print(f'{agave_nectar:.2f} cup(s) agave nectar')
print()

# PART TWO

# present: How many servings would you like to make?
wanted_servings = int(input('How many servings would you like to make?\n'))
juice_needed = wanted_servings*lemon_juice/servings
water_needed = wanted_servings*water/servings
agave_needed = wanted_servings*agave_nectar/servings

# present: Lemonade ingredients - yields X.00 servings
print()
print(f'Lemonade ingredients - yields {wanted_servings:.2f} servings')

# X.00 cup(s) lemon juice
print(f'{juice_needed:.2f} cup(s) lemon juice')

# X.00 cup(s) water
print(f'{water_needed:.2f} cup(s) water')

# X.00 cup(s) agave nectar
print(f'{agave_needed:.2f} cup(s) agave nectar')


# present: THE SAME ABOVE BUT Convert the ingredient measurements
# from (2) to gallons. Output the ingredients and serving size.
juice_gallons = juice_needed/16
water_gallons = water_needed/16
agave_gallons = agave_needed/16

# Lemonade ingredients - yields X.00 servings
print()
print(f'Lemonade ingredients - yields {wanted_servings:.2f} servings')

# X.00 gallon(s) lemon juice
print(f'{juice_gallons:.2f} gallon(s) lemon juice')

# X.00 gallon(s) water
print(f'{water_gallons:.2f} gallon(s) water')

# X.00 gallon(s) agave nectar
print(f'{agave_gallons:.2f} gallon(s) agave nectar')



