# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate( nums, k):
    n = len(nums)
    k = k % n

    # reverse the entire array
    reverse(nums,0, n-1)
    # reverse the first k elements
    reverse(nums, 0, k-1)
    # reverse the remaining elements from k to n-2
    reverse(nums, k, n-1)

# define helper function
def reverse(nums, start,end):
    while start < end:
        nums[start],nums[end] = nums[end], nums[start]
        start+=1
        end-=1

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums,k)
print("result" , nums)