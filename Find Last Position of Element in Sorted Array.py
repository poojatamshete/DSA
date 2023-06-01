#Find Last Position of Element in Sorted Array

arr = [1,2,2,2,3,4,4,4,5]

#steps
'''
1. check arr[mid]==x if this condition satisfies we will eliminate left side of array which occurs left side of mid.
2. low will be mid+1 we are moving to right side as chances of last occurence of x will be more on right side. 
'''

#code

def lastOccurence(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    while(low<=high): #base condition for binary search
        # calculate mid
        mid = low + (high-low)//2
         #check if x is <=arr[mid]
        if arr[mid]==x:
            ans = mid
            low = mid + 1
            continue
        if arr[mid]>x:
            high = mid -1
        else:
            low = mid + 1
    return ans

print("last occurrence of 4 is : ",lastOccurence(arr, 4))
print("last occurrence of 2 is : ",lastOccurence([2,2], 2))