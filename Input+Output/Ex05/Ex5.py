# Exercise 5: Accept a list of 5 float numbers as an input from the user

# Expected Output:
# [78.6, 78.6, 85.3, 1.2, 3.5]

array = []

for i in range(0,5):
    print('Me dá um número na posição %d:' % (i+1))
    item = float(input())
    array.append(item)

print("Lista Completa: ", array)