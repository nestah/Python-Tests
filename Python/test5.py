# given an array of integers, find two numbers such that they add to a specific target.
# you may assume that each input would have one solution, and you may not use the same element twice
# using the two-pointer approach

def two_sums(nums: list[int], target:int) ->list[int]:
    # sort the list and keep track of the original indices
    num_with_indices = sorted((num, i) for i, num in enumerate(nums))
    # initialize two pointers
    left, right = 0, len(nums) - 1
    # loop until the pointers meet
    while left < right:
        # calculate the sum of the numbers at the two pointers
        current_sum = num_with_indices[left][0] + num_with_indices[right][0]
        if current_sum == target:
            return num_with_indices[left][1], num_with_indices[right][1]
            
        elif current_sum < target:
            # move left pointer to the right
            left += 1
        else:
            # move the right pointer to the left to decrease the sum
            right -= 1
         
    
nums = [11, 2, 15, 7]
target = 17

result = two_sums(nums, target)

print(f"Result using two pointer approach{result}")