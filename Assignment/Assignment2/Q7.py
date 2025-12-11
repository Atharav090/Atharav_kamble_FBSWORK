# WAP to find sum of three digit numbers

# Take inputs
num = int(input("Enter three-digit number: "))
temp = num       

# perform operation
d1 = num % 10       #348 % 10 = 8
num = num // 10     #348 // 10 = 34
print(d1)
print(num)

d2 = num % 10       # 34 % 10 = 4
num = num //10      # 34 // 10 = 3
print(d2)
print(num)


d3 = num % 10       #3 % 10 = 3
num = num // 10     #3 // 10 = 0
print(d3)
print(num)

# display result
sum = d1 + d2 + d3
print(f'Addition of {temp} digits is {sum}.')






# Memory diagram
# ________________________________________________
# |                 |                            |
# |  sum = 4561     |    |15| 4561               |  
# |                 |    |0| 3456                |  
# |  d3 = 1235      |                            |  
# |                 |                            |  
# |                 |      |3| 1235              |  
# | d2 = 1234       |   |4| 1234                 |  
# |                 |                            |
# | temp = 6480     |  |34|  6480                |
# | d1 = 8384       |            |8|8384         | 
# |                 |                            | 
# | num = 2374      |        |348| 2374          |
# |       6480      |                            |
# |       1235      |                            |
# |       3456      |                            |
# |_________________|____________________________|
#    Stack                  Heap
