# Exercise 8: Format variables using a string.format() method.
# Write a program to use string.format() method to format the following three variables as per the expected output

# Given:
# totalMoney = 1000
# quantity = 3
# price = 450

# Expected Output:
# I have 1000 dollars so I can buy 3 football for 450.00 dollars.

totalMoney = int(input("\nTotal Money = "))
quantity = int(input("\nQuantity = "))
price = float(input("\nPrice = "))

print('I have %d dollars so I can buy %d football for %.2f dollars.' % (totalMoney,quantity,price))