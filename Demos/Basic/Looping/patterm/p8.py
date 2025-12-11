# my logic
# for i in range(1, 6):
#     k = 5
#     for j in range(1, i+1):
#         print(k, end= ' ')
#         k-=1
#     print()

# sir
for i in range(1,6):
    for j in range(5,5-i,-1):
        print(j, end=" ")
    print()