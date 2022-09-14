# Exercise 6: i the total number of digits in a number
# Write a program to i the total number of digits in a number using a while loop.

# For example, the number is 75869, so the output should be 5

n = int(input('Enter number '))
i = n
digits = 0
while(i != 0):
    i = i // 10
    digits += 1

print('The number %d has %d algorithms' % (n,digits))