def main():
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print("B. Selection = ", array)
    selectionArray = selectionSort(array)
    print("A. Selection = ", selectionArray)

def selectionSort(array):
    start = 0
    while(start <= len(array) - 1):
        box = start
        min = array[box] + 1
        index = 0
        while(box <= len(array) - 1):
            if(array[box] < min):
                min = array[box]
                index = box
            box += 1
        temp = array[index]
        array[index] = array[start]
        array[start] = min
        start += 1
    return array


main()