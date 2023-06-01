#Binary Search 
'''
Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. 
The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 
'''

#pseudo code

arr = [1,3,4,6,7,9]
x = 7

def BinarySearch(arr, x):
    n = len(arr)
    low = 0
    high = n-1

    while(low<=high): #base condition for binary search
        #calculate mid
        mid = low + (high-mid)//2
        
        if arr[mid] == x:
            return mid
        if x > arr[mid]: #means x lies on right half
            low = mid + 1
        else:
            high = mid -1 #means x lies on left half
    return -1