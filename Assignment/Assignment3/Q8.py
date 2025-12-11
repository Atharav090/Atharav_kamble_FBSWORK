# correct userid and password
c_userId = "admin"
c_password = "admin@123"
captcha = 54321

# take input from user
user_id = input("Enter Username: ")
password = input("Enter Password:")

# conditions
if(c_userId == user_id):
    if(c_password == password):
        print(f'{captcha}')
        cap_inp = int(input("Enter the above code: "))
        if(cap_inp == captcha):
            print(f'Logged in successfully.')
        else:
            print(f'captcha is wrong.')
    else:
        print(f'UserId or Password is incorrect.')
else:
    print(f'UserId or Password is incorrect.')

