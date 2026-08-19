class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        #if its not rotated

        while l < r:
            m = (l + r) // 2

            if (target != nums[m]):
                #find a sorted list
                if (nums[l] <= nums [m]):
                    #left side is a sorted list
                    if (nums[l] <= target <= nums[m]):
                        r = m
                    else:
                        l = m + 1
                else:
                    #right side is sorted
                    if (nums[m] <= target <= nums[r]):
                        l = m
                    else:
                        r = m - 1
            else:
                return m

        if (nums[l] == target):
            return l
        else:
            return -1






