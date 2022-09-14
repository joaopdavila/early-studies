def main():

    array = [8, 2, 4, 7, 1, 3, 9, 6, 5]
    print("The Array was: ", array)
    quickSort(array, 0, len(array)-1)
    print("Now it is: ", array)

def quickSort(array, start, finish):
    if(finish <= start):
        return

    pivotIndex = helper(array, start, finish)
    quickSort(array, start, pivotIndex - 1)
    quickSort(array, pivotIndex + 1, finish)  

def helper(array, start, finish):
    pivot = array[finish]
    j = start
    i = j-1
    temp = 0

    while (j < finish):
        if (array[j] >= pivot):
            j += 1
        else:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            j += 1

    i += 1
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    
    return i


main()