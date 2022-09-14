def main():
    array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    index = interpolationSearch(array,256)
    if(index != 1):
        print("Elemento achado em ", index)
    else:
        print("Elemento nao achado")

def interpolationSearch(array, value):
    high = len(array)-1
    low = 0

    while(value >= array[low] and value <= array[high] and low <= high):
        probe = int(low + (high - low) * (value - array[low])/(array[high] - array[low]))
        print("Probe = ", probe)
        if(array[probe] == value):
            return probe
        else:
            if(array[probe] < value):
                low = probe + 1
            else:
                high = probe - 1


main()