# Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.
num_of_stud = int(input("Enter total number of students: "))
avg_perc = 0
for i in range(1, num_of_stud + 1):
    m1 = int(input("Enter mark of student in subject 1: "))
    m2 = int(input("Enter mark of student in subject 2: "))
    m3 = int(input("Enter mark of student in subject 3: "))
    m4 = int(input("Enter mark of student in subject 4: "))
    m5 = int(input("Enter mark of student in subject 5: "))
    perc = ((m1 + m2 + m3 + m4 + m5)/500)*100
    print(f"Percentage of student is {perc}%")
    avg_perc += perc
avg_perc = avg_perc / num_of_stud
print(f"Average percentage of students is {avg_perc}%")