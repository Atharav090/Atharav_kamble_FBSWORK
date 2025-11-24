# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
# Taking input from the user
amount = int(input("Enter the amount: "))
amt = amount

# Performing the operation to find minimum number of notes

tt =  amount // 2000
amount = amount % 2000
# print(f'Remaining amount {amount}')

fh = amount // 500
amount = amount % 500
# print(f'Remaining amount {amount}')

th = amount // 200
amount = amount % 200
# print(f'Remaining amount {amount}')

h = amount // 100
amount = amount % 100
# print(f'Remaining amount {amount}')

ft = amount // 50
amount = amount % 50
# print(f'Remaining amount {amount}')

t = amount // 20
amount = amount % 20
# print(f'Remaining amount {amount}')

tn = amount // 10
amount = amount % 10
# print(f'Remaining amount {amount}')

# Final output
notes = tt + fh + th + h + ft + t+ tn
print(f'minimum number of notes for {amt} are {notes}')