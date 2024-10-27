# Given an integer array nums, return true if any value appears at least twice in the array,
#  and return false if every element is distinct.

class Solution(object):
    def contain_duplicates(self,nums):
        # create a set
        my_set = set()
        # iterate through the set to see if the num exists
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False    
# test
solution = Solution()
nums = [1,2,4,1]

result = solution.contain_duplicates(nums)
# print result of the function call
print(result)

 
 