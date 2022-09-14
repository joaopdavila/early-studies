# Exercise 18: Print the following pattern
# Write a program to print the following start pattern 
# using the for loop

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

n = int(input("Enter number: "))
k = n

for i in range(n+1):
    for j in range(i):
        print("*", end=' ')
    print("")

for i in range(1,n+1):
    for j in range(k-i,0,-1):
        print("*",end=' ')
    print()