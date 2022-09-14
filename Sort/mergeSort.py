def main():

    array = [8, 2, 5, 3, 4, 7, 6, 1]
    print("The Array was: ", array)
    mergeSort(array)
    print("Now it is: ", array)

def mergeSort(array):
    length = len(array)
    
    if (length <= 1):
        return

    middle = int(length/2)
    leftArray = [0]*middle
    rightArray = [0]*(length-middle)

    i = 0
    j = 0

    for i in range(length):
        if(i < middle):
            leftArray[i] = array[i]
        else:
            rightArray[j] = array[i]
            j += 1
        i += 1

    mergeSort(leftArray)
    mergeSort(rightArray)

    merge(leftArray, rightArray, array)

def merge(leftArray, rightArray, array):
    
    leftSize = int(len(array)/2)
    rightSize = len(array) - leftSize
    i = 0
    l = 0
    r = 0

    while(l < leftSize and r < rightSize):
        if(leftArray[l] < rightArray[r]):
            array[i] = leftArray[l]
            i += 1
            l += 1
        else:
            array[i] = rightArray[r]
            i += 1
            r += 1

    while(l < leftSize):
        array[i] = leftArray[l]
        i += 1
        l += 1

    while(r < rightSize):
        array[i] = rightArray[r]
        i += 1
        r += 1

main()