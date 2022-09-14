# Exercise 8: Print list in reverse order using a loop
# Given:

# list1 = [10, 20, 30, 40, 50]
# Expected output:

# 50
# 40
# 30
# 20
# 10

list1 = [10, 20, 30, 40, 50]

for x in range(len(list1)):

    maior = 0

    for i in range(len(list1)):
        if(list1[i] >= maior):
            maior = list1[i]

    print(maior)
    
    for j in range(len(list1)):
        if (list1[j] == maior):
            list1.pop(j)
