class Solution:
    def findMin(self, nums: List[int]) -> int:
        R = len(nums) - 1
        L = 0

        while L < R:
            mid = (R + L) // 2
            
            if (nums[mid] > nums[R]):
                L = mid + 1
            else:
                R = mid
        
        return nums[R]
        



        