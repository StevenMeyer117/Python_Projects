# Len's Slice.py is a program that utilizes python lists to organize sales data.  This is an intro-level project to
# practice concepts learned in Intro to Programming.

# List of pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# List of prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Number of slices that cost $2
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# 2D list of pizza slice associated with cost
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"],
                    [2, "mushrooms"]]
print(pizza_and_prices)

pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

print(cheapest_pizza)
print(priciest_pizza)

# Remove most expensive slice
pizza_and_prices.pop()
print(pizza_and_prices)

# Add peppers slice and price in appropriate location
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# Create list of three cheapest slices using slice method
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
