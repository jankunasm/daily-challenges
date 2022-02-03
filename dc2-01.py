# Self Dividing Numbers
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
# Example 1:
# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# Example 2:
# Input: left = 47, right = 85
# Output: [48,55,66,77]
 
# Constraints:
# 1 <= left <= right <= 104

#  Dylan Smith Solution

def selfDivRange(left, right):
    selfDivList=[]
    selfDiv=True
    for i in range(left,right+1):
        selfDiv=True
        for num in str(i):
            if int(num)== 0:
                selfDiv=False
            elif i % int(num) != 0:
                selfDiv=False
        if selfDiv==True:
            selfDivList.append(i)
    return selfDivList


#  Nate Welter Solution

# O(n*m) time | O(n) space (where n = length of range(left,right) and m = average amount of digits per number in range)
def sdn(left,right):
    res = []
    for num in range(left, right+1):
        if num < 10:
            res.append(num)
        else:
            temp = num
            while temp != 0:
                div = temp % 10
                if div != 0 and num % div == 0:
                    temp //= 10
                else:
                    break
            if temp == 0:
                res.append(num)
    return res
