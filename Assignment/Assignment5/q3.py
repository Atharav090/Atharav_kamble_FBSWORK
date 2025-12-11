# Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
no_of_passanger = int(input("Enter total number of passangers: "))
ticket_price = int(input("Enter ticket price: "))
total_ticket_cost = 0
for i in range(1, no_of_passanger+1):
    age = int(input("Enter the age of the passanger: "))
    if(age < 12):
        ticket = ticket_price * 0.70
    elif(age > 59):
        ticket = ticket_price * 0.50
    else: 
        ticket = ticket_price
    total_ticket_cost += ticket
print(f"Total cost of tickets for {no_of_passanger} passangers is {total_ticket_cost}")
    