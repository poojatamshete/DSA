#Algorithm

'''
1. Create a function findDivisionSum(nums, divisor) to return the division results sum.

2. Initialize variables:

    ans = -1, integer to store the lowest divisor which doesn't exceed threshold.
    low = 1, the lower bound of the search space of all possible divisors.
    high = max element of nums, the upper bound of the search space of all possible divisors.
3. Apply binary search on search space from low to high:

4. Initialize mid, with the middle value of search space i.e. (low + high) / 2.

5. Check if we use mid as the divisor, and if it does not exceed the threshold, then the answer can be mid.
So, update ans with mid, but we can also have smaller possible divisors, thus update high to mid - 1 (discarding the elements to the right of mid).
Otherwise, mid is too small, we need a bigger divisor, thus update low to mid + 1 (discard elements to the left of mid).

6. At the end, return ans.
'''

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        # Return the sum of division results with 'divisor'.
        def find_division_sum(divisor: int) -> int:
            result = 0
            for num in nums:
                result += ceil((1.0 * num) / divisor)
            return result
        
        ans = -1
        low = 1
        high = max(nums)
        
        # Iterate using binary search on all divisors.
        while low <= high:
            mid = (low + high) // 2
            result = find_division_sum(mid)
            # If current divisor does not exceed threshold, 
            # then it can be our answer, but also try smaller divisors
            # thus change search space to left half.
            if result <= threshold:
                ans = mid
                high = mid - 1
            # Otherwise, we need a bigger divisor to reduce the result sum
            # thus change search space to right half.
            else:
                low = mid + 1
        
        return ans