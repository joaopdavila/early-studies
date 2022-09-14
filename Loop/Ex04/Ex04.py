# Exercise 4: Write a program to print multiplication table of a given number
# For example, num = 2 so the output should be

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

n = int(input('Enter number '))

for i in range (10):
    print(n * (i+1))