# Exercise 9: Check file is empty or not
# Write a program to check if the given file is empty or not

path = input("Qual o File Path? ")

with open(path,'r') as fp:
    content = fp.readlines()
    if(content == []):
        print('Empty')
    else:
        print('Not Empty')