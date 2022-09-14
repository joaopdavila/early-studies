# Exercise 11: Write a program to display all prime numbers within a range
# Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers

# Examples:

# 6 is not a prime mumber because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply together to make it.
# Given:


# # range
# start = 25
# end = 50
# Expected output:

# Prime numbers between 25 and 50 are:
# 29
# 31
# 37
# 41
# 43
# 47


start = int(input('start = '))
end = int(input('end = '))

for i in range(start,end+1):
    j = i - 1
    cont = 0
    while(j > 1):
        if(i % j == 0):
            cont +=1
        j -= 1
    if(cont == 0):
        print(i)