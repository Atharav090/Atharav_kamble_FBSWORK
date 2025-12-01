# WAP to check if user has entered correct userid and password
# correct userid and password
c_userId = "admin"
c_password = "admin@123"

# take input from user
user_id = input("Enter Username: ")
password = input("Enter Password:")

# conditions
if(c_userId == user_id):
    if(c_password == password):
        print(f'Logged in')
else: 
    print(f'User id or password is wrong.')