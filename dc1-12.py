# Given two non-empty arrays of integers(numbers), write a function that 
# determines whether the second array is a subsequence of the first one.
# A subsequence of an array is a set of numbers that aren’t necessarily 
# adjacent in the array but that are in the same order as they appear in 
# the array. For instance, the numbers [1,3,4] form a subsequence of the 
# array [1,2,3,4], and so do the numbers [2,4]. Note that a single number 
# in an array and the array itself are both valid subsequences of the array.
# ( [1],[2],[3],[4]and [1,2,3,4] are all valid subsequences of [1,2,3,4] )
# Sample Output

# My Solution
array = [5,1,22,25,6,-1,8,10]
subsequence = [1,6,-1,10]
Answer: True

listcheck = []

def arraychecker(array, subseq):
    for num in array:
        if num in subseq:
            listcheck.append(num)
    if listcheck == subseq:
        return True
    else:
        return False

print(arraychecker(array, subsequence))


# Jon Watts Solution

# def subsequence(arr1, arr2):
#     arr1EnumDict = dict([(y,x) for x,y in enumerate(arr1)])
#     orderCheck1 = ''
#     for i in arr2:
#         if i not in arr1EnumDict:
#             return False
#         if orderCheck1 != '':
#             if orderCheck1 > arr1EnumDict.get(i):
#                 return False    
#         orderCheck1 = arr1EnumDict.get(i)
#     return True
# print(subsequence([5,1,22,25,6,-1,8,10],[1,6,-1,10]))
# print(subsequence([5,1,22,25,6,-1,8,10],[1,6,-1,11]))
# print(subsequence([5,1,22,25,6,-1,8,10],[1,-1,6,10]))


# Joshua Cunningham Solution

# def subseq(a1, a2):
#     return [num for num in a1 if num in a2] == a2            
# print(subseq([5,1,22,25,6,-1,8,10], [1,6,-1,10]))


# Nate Welter Solution and second Nate Welter but explained line by line

# O(n) time | O(1) space (where n = len(array))
# def validSubseq(array, sequence):
#     i = 0 
# 	j = 0 
# 	while i < len(array):
# 		if array[i] == sequence[j]:
# 			i += 1
# 			j += 1
# 			if j == len(sequence):
# 				return True
# 		else:
# 			i += 1
# 	return False

# # Notes line-by-line here
# def validSubseq(array, sequence):
#     i = 0 #array index
# 	j = 0 # sequence index
# 	# loop over array, value by value
# 	while i < len(array):
# 		# once we find sequence[j] in array, move forward to the next val in sequence
# 		# and the next val in array
# 		if array[i] == sequence[j]:
# 			i += 1
# 			j += 1
# 			# if we have found the full subsequence - true
# 			if j == len(sequence):
# 				return True
# 		# even if we did not find the value on this pass, keep moving forward in array
# 		else:
# 			i += 1
# 	# if we make it through the full array without triggering a return - this is False
# 	return False