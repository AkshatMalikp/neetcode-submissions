class Solution:

    def siuuuu(self, nums:List[int], k: int, finalanswer: List[List[int]],tempanswer:List[int],summ: int,target: int):
        if k==len(nums):
            finalanswer.append(tempanswer.copy())
            return




        tempanswer.append(nums[k])
        summ=summ+nums[k]
        if summ <= target:
            self.siuuuu(nums,k+1,finalanswer,tempanswer,summ,target)
            self.siuuuu(nums,k,finalanswer,tempanswer,summ,target)
        tempanswer.pop()
        summ=summ-nums[k]
        self.siuuuu(nums,k+1,finalanswer,tempanswer,summ,target)



    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        finalanswer=[]
        self.siuuuu(nums,0,finalanswer,[],0,target)

        finalfinalanswer=[]

        for i in finalanswer:
            sumsto=0
            for j in i:
                sumsto=sumsto+j
            if sumsto == target:

                finalfinalanswer.append(i)    

        result = list(map(list, set(map(tuple, finalfinalanswer))))
        return result



        