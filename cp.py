def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    print(arr)


if __name__ == "__main__":
    arr = []
    for i in range(10):
        arr.append(input("Enter element" + str(i+1)))
    bubbleSort(arr)

    b = []


    c = [1, 3, 4]
