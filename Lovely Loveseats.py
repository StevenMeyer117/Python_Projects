# 'Lovely Loveseats.py' is an introduction project to programming.  In this project I will be storing names and prices
# of a furniture store's catalog in variables.  I will then process the total price and item list of customers, printing
# them to the output terminal

# Inventory descriptions
lovely_loveseat_description = ("Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 "
                               "inches deep. Red or white.")

stylish_settee_description = ("Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches"
                              " deep. Black.")

luxurious_lamp_description = ("Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.")


# Inventory price
lovely_loveseat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15

# Sales tax
sales_tax = 0.088

# Keep running tally of first customer's purchases and expenses
customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# Calculate customer_one sales tax
cutsomer_one_tax = customer_one_total * sales_tax
customer_one_total += cutsomer_one_tax

# Print out receipt of customer_one's items
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)