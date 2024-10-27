# solving using hash map(dictionary).
# this is a more efficient approach that reduces time complexity from 0(n^2) to 0(n)
# instead of using two loops we can use a dictionary to store the difference between
# the target and the current number.

def two_nums(nums: list[int], target:int) ->list[int]:
    # creat a dictionary to store the number we need to find and its index
    num_to_index = {}
    # loop thru list once
    for i, num in enumerate(nums):
        # calculate difference between target and current number
        difference = target - num
        # if the current number is already in the dictionary return the pair
        if num in num_to_index:
            return [num_to_index[num], i]
        else:
            print("pair not reached")
        # otherwise store the difference and currnt index
        num_to_index[difference] = i
nums = [1,4,6,5,7,9]
target = 5

result = two_nums(nums, target)
print(f"Hash map approach: {result}")



