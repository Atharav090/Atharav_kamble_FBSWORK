start = int(input("Enter start range: "))
end = int(input("Enter end range: "))
for num in range(start, end + 1):
    temp = num
    count = 0
    while(temp > 0):
        temp //= 10
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
           print(num)