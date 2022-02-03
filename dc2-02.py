# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:
# Input: nums = [1]
# Output: 1
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

#  Hamed Solution

def contig_array(array):
    max_num   = 0
    
    for num1 in range(len(array)):
        array2  = []
        
        for num2 in array[num1::]:
            array2.append(num2)
            
            if sum(array2) > max_num:
                max_num = sum(array2)
            
    return(max_num)


# Jon Watts Solution

def FindLargestSubArraySum(arr):
    l = 0
    r = 0
    largest = arr[0]   

    while l < len(arr):
        while r < len(arr):
            if sum(arr[l:r+1]) > largest:
                largest = sum(arr[l:r+1])
                r += 1
            else:
                r +=1
        l += 1
        r = l
    return largest


print(FindLargestSubArraySum([-2,1,-3,4,-1,2,1,-5,4]))
print(FindLargestSubArraySum([4,-1,2,1]))
print(FindLargestSubArraySum([1]))
print(FindLargestSubArraySum([-1]))
print(FindLargestSubArraySum([5,4,-1,7,8]))