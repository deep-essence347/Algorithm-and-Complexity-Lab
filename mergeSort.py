import math

# Merge Function
def merge(arr,lb,mid,ub):

	# n1 and n2 variables that define the length of left and right arrays
	n1 = mid-lb+1 
	n2 = ub - mid

	# L and R are two subarrays of arr that is divided by mid index of the array and adding infinity to end of each sub array.
	# L is left half of the array while R is the right half
	L=arr[lb:lb+n1]+[math.inf]
	R=arr[mid+1:mid+n2+1]+[math.inf]

	i,j=0,0
	
	# To merge each subarray, we compare the elements of two subarrays one by one and add the smaller value to array until all the elements are sorted.
	for k in range(lb,ub+1):
		if(L[i]<=R[j]):
			arr[k]=L[i]
			i+=1
		else:
			arr[k]=R[j]
			j+=1

def mergeSort(arr,lb,ub):
	if(lb<ub):
		mid = math.floor((lb+ub)/2)
		mergeSort(arr,lb,mid)
		mergeSort(arr,mid+1,ub)
		merge(arr,lb,mid,ub)
		
arr =[]

for i in range(0,10):
    elem = int(input("Enter element: "))
    arr.append(elem)

print("Unsorted Array:::")
print(arr)

mergeSort(arr,0,len(arr)-1)

print("Sorted Array:::")
print(arr)
