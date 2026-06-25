class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set()
        num=0
        for num in nums:
            if num in a:
                return True
            a.add(num)
        return False


        