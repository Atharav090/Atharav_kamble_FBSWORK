# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

# take inputs
age1 = int(input("Enter the age of person1: "))
age2 = int(input("Enter the age of person2: "))
age3 = int(input("Enter the age of person3: "))
age4 = int(input("Enter the age of person4: "))
age5 = int(input("Enter the age of person5: "))

amount  = float(input("Enter the ticket amount: "))
total_amount = 0

# conditions
if(age1 < 12):
    total_amount += amount * 0.7
elif(age1 > 59):
    total_amount += amount * 0.5
else:
    total_amount += amount

if(age2 < 12):
    total_amount += amount * 0.7
elif(age2 > 59):
    total_amount += amount * 0.5
else:
    total_amount += amount

if(age3 < 12):
    total_amount += amount * 0.7
elif(age3 > 59):
    total_amount += amount * 0.5
else:
    total_amount += amount

if(age4 < 12):
    total_amount += amount * 0.7
elif(age4 > 59):
    total_amount += amount * 0.5
else:
    total_amount += amount

if(age5 < 12):
    total_amount += amount * 0.7
elif(age5 > 59):
    total_amount += amount * 0.5
else:
    total_amount += amount

print(f'total amount of ticket for 5 people is {total_amount}')