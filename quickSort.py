def partition(arr,l,u):
    x=arr[u]
    i=l-1
    for j in range(l,u):
        print('i - ',i, ':',arr[i])
        if(arr[j]<=x):
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
        print('j - ',j, ':',arr[j])
        print(arr)
    
    arr[i+1],arr[u] = arr[u],arr[i+1]
    print('i - ',i, ':',arr[i])
    print('j - ',j, ':',arr[j])
    print('End',arr)
    return i+1

def quickSort(arr,l,u):
    if(l<u):
        pivot=partition(arr,l,u)
        print(pivot, ': ',arr[pivot])
        quickSort(arr,l,pivot-1)
        quickSort(arr,pivot+1,u)

arr =[2, 67, 45, 3, 24, 12, 50, 3]

# for i in range(0,10):
#     elem = int(input("Enter element: "))
#     arr.append(elem)

print("Unsorted Array::: ")
print(arr)

quickSort(arr,0,len(arr)-1)

print("Sorted Array::: ")
print(arr)
