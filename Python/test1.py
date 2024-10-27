# Two Sum Problem
# given an array of integers, find two numbers such that they add to a specific target.
# you may assume that each input would have one solution, and you may not use the same element twice

# def two_sums(nums: list[int], target:int) ->list[int]:
#     pass

def two_sums(nums: list[int], target:int) -> list[int]:
 

    # outer loop, loop thru each element in the list
    for i in range(len(nums)):
        # for each element check all other elements
        for j in range(i+1, len(nums)):
            # if the two elements sum up to the target, return their indices 
            if nums[i] + nums[j] == target:
                return [i,j]
    
nums = [2,7,8,9,6,7]
target = 10

result = two_sums(nums, target)

print(f"Result using brute force:{result}")


