class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,j in enumerate(nums):
            diff=target-j
            if diff in hash:
                return [hash[diff],i]
            hash[j]=i
        return