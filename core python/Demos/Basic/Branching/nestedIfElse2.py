# WAP to print grade of given percentage(int value)
marks = int(input("Enter final percentage: "))

if(marks < 35 ):
    print("Fail")
else: 
    if(marks > 70):
        if(marks > 80):
            if(marks > 90):
                print("A grade")
            else: 
                print("B grade")
        else: 
            print("C grade")
    else: 
        print("D grade")
