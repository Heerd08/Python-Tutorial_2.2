# 11. Highest Selling Product
# Problem:
# You are given a list of tuples where each tuple represents (product_name, quantity_sold). Return the product name with the highest total sales.
# Input:
# [("Pen", 10), ("Pencil", 25), ("Pen", 15)]
# Output:
# "Pen"

sales = [("Pen", 10), ("Pencil", 25), ("Pen", 15)]
total_sales = {}

for product, quantity in sales:
    if product in total_sales:
        total_sales[product] += quantity
    else:
        total_sales[product] = quantity

max_product = max(total_sales, key=total_sales.get)
print(max_product)
