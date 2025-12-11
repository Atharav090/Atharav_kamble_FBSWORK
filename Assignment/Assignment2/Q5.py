# WAP to calculate selling price of book based on cost price and discount.
# take inputs
cost_price = float(input("Enter the cost price of the book: "))
discount_percentage = float(input("Enter the discount percentage: "))
# calculate discount amount
discount_amount = (discount_percentage / 100) * cost_price
# calculate selling price
selling_price = cost_price - discount_amount
# display result
print(f'The selling price of the book is {selling_price}')
