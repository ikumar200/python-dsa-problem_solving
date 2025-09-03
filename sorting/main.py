# selection sort
def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr

# bubble sort
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

# insertion sort
def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr 

# merge sort


if __name__=="__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    # sorted_arr=bubbleSort(arr)
    # sorted_arr=selectionSort(arr)
    sorted_arr=insertionSort(arr)
    print("Sorted array is:", sorted_arr) 