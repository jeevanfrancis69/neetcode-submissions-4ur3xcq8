class Solution:
    def findMin(self, nums: List[int]) -> int:
        R = len(nums) - 1
        L = 0

        # while L < R:
        #     mid = (R + L) // 2
            
        #     if (nums[mid] > nums[R]):
        #         L = mid + 1
        #     else:
        #         R = mid
        
        # return nums[R]
        
        res = nums[0]

        while L <= R:
            if nums[L] < nums[R]:
                res = min(res , nums[L])
                break
            
            m = (L + R) // 2

            res = min(res, nums[m])

            if (nums[m] >= nums[L]):
                L = m + 1
            else:
                R = m - 1
        return res


        