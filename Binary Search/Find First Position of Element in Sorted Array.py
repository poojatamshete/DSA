#Find First Position of Element in Sorted Array

arr = [1,2,2,2,3,4,4,4,5]

#steps
'''
1. check arr[mid]>=x if this condition satisfies we will eliminate right side of array which occurs right after mid.
2. high will be mid-1 we are moving to left side as chances of first occurence of x will be more on right side. 
'''

#code

def fiirstOccurence(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    while(low<=high): #base condition for binary search
        # calculate mid
        mid = low + (high-low)//2
         #check if x is <=arr[mid]
        if arr[mid]==x:
            ans = mid
            high = mid - 1
            continue
        if arr[mid]>x:
            high = mid -1
        else:
            low = mid + 1
    return ans

print("first occurrence of 4 is : ",fiirstOccurence(arr, 4))
print("first occurrence of 2 is : ",fiirstOccurence(arr, 2))