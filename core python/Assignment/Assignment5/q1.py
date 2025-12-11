# Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.
originalUser = "admin"
originalPass = "admin@123"
for i in range(1, 3):
    user = input("Enter username: ")
    passwd = input("Enter password:") 
    if(user == originalUser and passwd == originalPass):
        print(f"Successfully logged in.")
        break
    else: 
        print(f"Invalid username or password.")