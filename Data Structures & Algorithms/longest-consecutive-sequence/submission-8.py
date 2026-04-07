class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        
        lengthList = []
        if not nums:
            return 0

        for numbers in setNums:
            if numbers - 1 not in setNums:
                startNumber = numbers
                length = 1       
                while startNumber + length in setNums:
                    length += 1
                lengthList.append(length)
        
        return max(lengthList)