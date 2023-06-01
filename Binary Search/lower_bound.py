#lower bound

arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
x = 12

def ub(arr,n,x):
    low = 0
    high = n-1
    ans = n
    while(low<=high):
        mid = low + (high-low)//2

        if (arr[mid]>=x):
            ans = mid
            high = mid - 1

        else:
            low = mid + 1
    return ans

print(ub(arr,n,x))
        