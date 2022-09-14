from random import randint

# generate array
def randomarray(min, n):
    array = []
    for i in range(n):
        array.append(min + randint(0, 50))
    return array

def getdiff(array):
    diff = []
    for i in range(1,len(array)):
        diff.append(array[i]-array[i-1])
    return diff

def main():
    # array = randomarray(1,15)
    array = [3, 24, 46, 51, 46, 34, 44, 13, 15, 8, 5, 37, 44, 15, 24, 23, 40]
    diff = getdiff(array)
    menor = min(diff)
    print(array)
    print(diff)
    print(menor) 

main()