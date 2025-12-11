# Identity Operators

x=10
y=10
li1 = [10,20,30]
li2 = [10,20,30]


# is
print(id(x))
print(id(y))
print(x is y)
print(id(li1))
print(id(li2))
print(li1 is li2)



# Memory diagram
# ________________________________________________
# |                 |                            |  
# | li2 = 6480      |  |10|20|30|  6480          |
# | li1 = 8384      |            |10|20|30| 8384 | 
# |                 |                            |
# | y = 1407        |                            |
# | x = 1407        |         10 = 1407          |
# |_________________|____________________________|
#    Stack                  Heap



# is not
print(li1 is not li2)