def main():
    array = [1, 8, 9, 2, 7, 3, 6, 4, 5]
    print("B. Bubble = ", array)
    bubbleArray = bubbleSort(array)
    print("A. Bubble = ", bubbleArray)

def bubbleSort(array):
    k = 0
    while(k <= len(array)-1):
        i = 0
        j = 1
        while(j <= len(array)-1):
            if(array[i] > array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
            i += 1
            j += 1
        k += 1
    return array

main()