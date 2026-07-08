class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lis=[]
        n=len(nums)
        for i in range(n):
            if nums[i]  in lis:
                return True
            else:
                lis.append(nums[i])
                
        return False