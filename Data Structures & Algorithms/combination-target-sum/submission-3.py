class Solution:

    def siuuuu(self, nums:List[int], k: int, finalanswer: List[List[int]],tempanswer:List[int],summ: int,target: int):
        if k==len(nums):
            if summ==target:
               finalanswer.append(tempanswer.copy())
            return

        if summ > target:
            return    




        tempanswer.append(nums[k])
        summ=summ+nums[k]
        self.siuuuu(nums,k,finalanswer,tempanswer,summ,target)
        tempanswer.pop()
        summ=summ-nums[k]
        self.siuuuu(nums,k+1,finalanswer,tempanswer,summ,target)



    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        finalanswer=[]
        self.siuuuu(nums,0,finalanswer,[],0,target)
        result = list(map(list, set(map(tuple, finalanswer))))
        return result



        