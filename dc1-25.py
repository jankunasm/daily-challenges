# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Jon Watts Solution

def reverseVowels(string):
    vowelList = []
    vowelSet = {"a", "e", "i", "o", "u"}
    for letter in string:
        if letter in vowelSet:
            vowelList.append(letter)
    for i in range(len(string)):
        if string[i] in vowelSet:
            string = string[:i] + vowelList.pop(-1) + string[i+1:]
    return string

# Dylan Smith Solution

def reverseVowells(astring):
    vowells=[]
    for letter in astring:
        if letter.lower() in 'aeiou':
            vowells.append(letter)
    vowells= vowells[::-1]
    answer=''
    count=0
    for letter in astring:
        if letter.lower() in 'aeiou':
            answer+=vowells[count]
            count+=1
        else:
            answer+=letter
    return answer
    

# Nate Welter Solution

def reverseVowels(s):
        vow = set('aeiouAEIOU')
        s_list = list(s)
        l = 0
        r = len(s_list)-1
        while l < r:
            if s_list[l] in vow and s_list[r] in vow:
                s_list[l], s_list[r] = s_list[r], s[l]
                l += 1
                r -= 1
            if s_list[l] not in vow:
                l += 1
            if s_list[r] not in vow:
                r-= 1
        return ''.join(s_list)
