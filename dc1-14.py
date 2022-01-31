# Find the Longest Substring w/o Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Examples:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Jon Watts Solution

# def longestSubString(string):
#     substring = set()
#     substringList = []
#     for letter in string:
#         if letter not in substring:
#             substring.add(letter)
#         else:
#             substringList.append(len(substring))
#             substring = set(letter)
#     substringList.append(len(substring))        
#     return max(substringList)
# print(longestSubString("abcabcbb"))
# print(longestSubString("bbbbb"))
# print(longestSubString("pwwkew"))
# print(longestSubString("abcd"))
# print(longestSubString("aabcd"))


# Nate Welter Explained Soltuion

#commented version

def longestSub(s):
	# pointer to keep track of current first unique character
    left = 0
	# pointer to keep track of our current place in the loop
    right = 0
	# set to add every character to (eventually going to have a membership check in constant time)
    subs = set()
	# variable to hold the longest substring we've seen so far - start at 0
    longest = 0
	# while the right pointer is still a valid index in our string...
    while right < len(s):
		# if we have not seen this letter yet...
        if s[right] not in subs:
			# compare our current longest substring to the left - right index
            longest = max(longest, right - left+1)
			# add our new letter to the set
            subs.add(s[right])
        else:
			# if it is already in our set, that means we've seen it in this current substring.
			# do away with the duplicate by moving the left pointer one place to the right.
			# again - compare the longest substring to our new substring.
            longest = max(longest, right - left+1)
            left += 1
		# keep moving forward to the next character, regardless
        right += 1
    return longest