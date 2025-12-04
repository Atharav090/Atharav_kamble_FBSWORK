# A man goes for shopping. He buys 5 products. Accept the price of all products and dsplay total bill after adding 18% GST

# take price of 5 products
p1 = int(input("Enter the price of product 1: "))
p2 = int(input("Enter the price of product 2: "))
p3 = int(input("Enter the price of product 3: "))
p4 = int(input("Enter the price of product 4: "))
p5 = int(input("Enter the price of product 5: "))

total_bill_without_gst = p1 + p2 + p3 + p4 + p5
gst = total_bill_without_gst * 0.18
total_bill_with_gst = total_bill_without_gst + gst
print(f'Total bill after adding 18% gst is {total_bill_with_gst}')