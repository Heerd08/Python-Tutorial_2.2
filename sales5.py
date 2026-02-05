# 5. Product Sales Aggregator

# Problem:
# Given a list of tuples containing product names (string) and quantity sold (int), create a dictionary that stores the total quantity sold for each product.

# Input:
# [("Pen", 10), ("Pencil", 5), ("Pen", 15)]

# Output:
# {"Pen": 25, "Pencil": 5}


sales = [("Pen", 10), ("Pencil", 5), ("Pen", 15)]
total_sales = {}

for product, qty in sales:
    if product in total_sales:
        total_sales[product] += qty
    else:
        total_sales[product] = qty

print(total_sales)
