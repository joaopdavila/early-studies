# Exercise 9: Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]
# Expected Output:

# 24

def maior(array):
    max = 0
    for i in range(len(array)):
        if(array[i] > max):
            max = array[i]
    return max

x = [4, 6, 8, 24, 12, 2]
print(maior(x))