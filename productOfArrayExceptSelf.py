'''
input : array nums
return : array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]


'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        lst = []
        l = 0
        r = len(nums)-1
        hasmap = {}
        lprod = 1
        rprod = 1

        for index,i in enumerate(nums):

            if l == index:
                hasmap[index] = hasmap.get(index,1) * lprod
            if r == len(nums)-index-1:
                hasmap[len(nums)-index-1] = hasmap.get(len(nums)-index-1,1) * rprod

            lprod = lprod * i
            rprod = rprod * nums[r]
            l+=1
            r=r-1
        return [hasmap[i] for i in hasmap]


