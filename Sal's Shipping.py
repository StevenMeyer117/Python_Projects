# Sal's Shipping.py is a program that simulates a shipping company.  The company offers shipping via three methods:
# Ground Shipping, Ground Shipping Premium and Drone Shipping.  The program takes the weight of a package and determines
# Which method would be the cheapest by displaying shipping rates.  This program is practice using control flow and if/
# elif/else statements.

weight = 41.5

# Ground Shipping
if weight <= 2:
    cost = weight * 1.50 + 20.00
elif weight <= 6:
    cost = weight * 3.00 + 20.00
elif weight <= 10:
    cost = weight * 4.00 + 20.00
else:
    cost = weight * 4.75 + 20.00

ground_shipping = "Ground Shipping cost: $" + str(cost)
print(ground_shipping)

# Premium Ground Shipping
premium_ground_shipping = "Premium Ground Shipping cost: $" +str(125)
print(premium_ground_shipping)

# Drone Shipping
if weight <= 2:
    cost = weight * 4.50
elif weight <= 6:
    cost = weight * 9.00
elif weight <= 10:
    cost = weight * 12.00
else:
    cost = weight * 14.25

drone_shipping = "Drone Shipping cost: $" + str(cost)
print(drone_shipping)
