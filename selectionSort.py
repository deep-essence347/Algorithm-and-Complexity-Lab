import random

# Function to sort the array
def selectionSort(arr):
    for i in range(0,len(arr)-1):
        m=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[m]):
                m=j
        temp = arr[i]
        arr[i]=arr[m]
        arr[m]=temp
    return arr

arr = random.sample(range(1,101),100)

# Printing unsorted array
print("Unsorted Array:::")
print(arr)

sortedArray = selectionSort(arr)

#Printing Sorted Array
print("Sorted Array:::")
print(sortedArray)