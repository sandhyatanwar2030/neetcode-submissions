class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lis=[]
        n=len(nums)
        for i in range(n):
            if nums[i] not in lis:
                lis.append(nums[i])
            else:
                return True
        return False