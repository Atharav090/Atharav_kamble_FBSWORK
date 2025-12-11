# WAP to print Armstrong number within a given range
start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))
for num in range(start, end+1):
    temp = num
    count = 0
    while(temp > 0):
        temp = temp // 10
        count += 1 
    temp = num
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp //= 10
        multi = 1
        for i in range(count):
            multi = multi * d
        sum = sum + multi
    if(sum == num):
        print(f"{num}")

