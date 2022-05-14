import random

# Function to sort the array
def insertionSort(arr):
    count = 1
    for j in range(1, len(arr)):
        key = arr[j]
        i=j-1
        while i>=0 and arr[i]>key:
            arr[i+1]=arr[i]
            i=i-1
            print(count,': ',arr)
            count = count+1
        arr[i+1]=key
        
        print(count,': ',arr)
        count = count+1
    return arr

# arr = random.sample(range(1,101),100)
arr = [55, 32, 45, 12, 11, 33, 14]

# Printing unsorted array
print("Unsorted Array:::")
print(arr)

#Calling a function to sort the array
sortedArray = insertionSort(arr)

#Printing Sorted Array
print("Sorted Array:::")
print(sortedArray)