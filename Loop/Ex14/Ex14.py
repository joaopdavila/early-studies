# Exercise 14: Reverse a given integer number
# Given:

# 76542

# Expected output:

# 24567

a = int(input("Enter number: "))
b = 0

while(a != 0):
    b = ((10*b) + (a%10))
    a = a // 10

print(b)