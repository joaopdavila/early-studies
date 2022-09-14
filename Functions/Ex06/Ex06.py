# Exercise 6: Create a recursive function
# Write a program to create a recursive function to 
# calculate the sum of xbers from 0 to 10.


# A recursive function is a function that calls itself, 
# again and again.

# Expected Output:

# 55

def soma(x):
    if x:
        return x + soma(x - 1)
    else:
        return 0

n = int(input("Enter number: "))

print(soma(n))