#upper bound

#steps
'''
1. here we need to find first element which is greater than x , first element means the element which is greater right after x in sorted array.
2. firstly we will check if mid <= x if so we will eliminate left array. as we want to find greater element than x so low = mid +1
3. if we found mid > x then we will update ans = mid and high = mid - 1 as we we dont want more higher elements we will search higher element in left half now.

if still has confusion refer https://www.youtube.com/watch?v=SpS9dMj0B_Y at 1:19 minutes
'''

arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
x = 7

def ub(arr, n, x):

    low = 0
    high = n-1
    ans = n

    while(low<=high):
        mid = low + (high-low)//2

        if (arr[mid]<=x):
            low = mid +1
        else:
            ans = mid
            high = mid -1
    return ans

print(ub(arr, n, x))