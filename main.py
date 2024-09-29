"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 0
# Number of characters.
numChars = 18
# Color of characters.
color = "black"
# Type of wood.
woodType = "oak"

# Write assignment and if statements here as appropriate.
MIN_CHARGE = 35.00

if numChars > 5:
  charCharge = (numChars - 5) * 4
else:
  charCharge = 0

if woodType == "oak":
  woodTypeCharge = 20
else:
  woodTypeCharge = 0

if color == "gold":
  colorCharge = 15
else:
  colorCharge = 0

totalCharge = MIN_CHARGE + charCharge + woodTypeCharge + colorCharge



# Output Charge for this sign.
print("The charge for this sign is $" + str(totalCharge))