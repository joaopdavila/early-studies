def main():
    array = [6, 1, 7, 4, 2, 9, 8, 5, 3]
    print("B. Insertion = ", array)
    insertionArray = insertionSort(array)
    print("A. Insertion = ", insertionArray)

def insertionSort(array):
    i = 1
    while(i <= len(array) - 1):
        temp = array[i]
        j = i - 1
        while(j >= 0):
            if(array[j] > temp):
                array[j+1] = array[j]
                array[j] = temp
            j -= 1
        i += 1
        
    return array

main()