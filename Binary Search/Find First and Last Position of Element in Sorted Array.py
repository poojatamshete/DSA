#Find First and Last Position of Element in Sorted Array

'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low = 0
        high = len(nums) - 1
        fPos = -1
        while(low<=high):
            #first occurrence
            mid = low + (high-low)//2
            if(nums[mid]==target):
                fPos = mid
                high = mid -1
                continue
            if(target > nums[mid]):
                low = mid +1
            else:
                high = mid-1

        low = 0
        high = len(nums) - 1
        lPos = -1
        while(low<=high):
            #last occurrence
            mid = low + (high-low)//2
            if (nums[mid]==target):
                low = mid +1
                lPos = mid
                continue
            if (target > nums[mid]):
                low = mid + 1
            else:
                high = mid - 1

        
        return [fPos, lPos]



