# Exercise 8: Generate a Python list of all the even 
# numbers between 4 to 30
# Expected Output:

# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

def par(num):
    if(num % 2 == 0):
        return True
    else:
        return False

def criar(start,finish):
    array = []
    for i in range(start,finish+1):
        array.append(i)
    return array

def add(array):
    arr = []
    for i in range(len(array)):
        if(par(array[i]) == True):
            arr.append(array[i])
        else:
            continue
    return arr


array = criar(4,30)
print(add(array))