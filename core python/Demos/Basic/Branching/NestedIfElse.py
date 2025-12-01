# to find gender and age is eligible for marriage

gender = input("Enter gender (M/F): ")
age = int(input("Enter age: "))

#  Nested If Else: 
if(gender == "M"):
    if(age >= 21):
        print("Eligible for marriage.")
    else:
        print("not eligible for marriage.")
else:
    if(age >= 18):
        print("Eligible for marriage.")
    else:
        print("not eligible for marriage.")