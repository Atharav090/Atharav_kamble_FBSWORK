# Input 5 subject marks from user and display grade(eg.First class,Second class ..)
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

perc = ((m1 + m2 + m3 + m4 + m5)/500) * 100
print(f'Percentage of the sudents is {perc}%')

if(perc < 35):
    print("failed")
elif(perc >= 35 and perc < 50):
    print("Grade D")
elif(perc >= 50 and perc < 60):
    print("Grade C")
elif(perc >= 60 and perc < 80):
    print("Grade B")
elif(perc >= 80):
    print("Grade A")
