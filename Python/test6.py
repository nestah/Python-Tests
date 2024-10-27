# remove duplicate from sorted array

def remove_duplicate(nums:list[int])->list[int]:
    # check if array is empty
    if not nums:
        return 0
    # initialize k with 0
    k=0
    # iterate through the list
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]

    return k + 1   
nums = [1,1,2,3,4,4]
length = remove_duplicate(nums)

print(nums[:length])