# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# Examples:
# Input: s = "()"
# Output: true
# Input: s = "()[]{}"
# Output: true
# Input: s = "(]"
# Output: false

# Jon Watts Solution

def bracketCheck2(string):
    checkDict = {'(':')',
                '[':']',
                '{':'}',
                }
    while string != '':
        if len(string) == 1:
            return False
        elif string[0] not in checkDict:
            return False
        elif string[1] == checkDict[string[0]]:
            string = string[2:]
        else:
            return False
    return True

print(bracketCheck2("()"))

print(bracketCheck2("()[]{)"))


# O(n) time | O(n) Space (where n = len(s))
def checkBrackets(s):
    pairs = {')' : '(', ']' : '[', '}' : '{'}
    last_open = []
    for char in s:
        if char not in pairs:
            last_open.append(char)
        else:
            if not last_open or last_open[-1] != pairs[char]:
                return False
            last_open.pop()
    return len(last_open) == 0

# Nate Welter Explained Solution

# Commented version
def checkBrackets(s):
	# dictionary to hold corresponding pairs
    pairs = {')' : '(', ']' : '[', '}' : '{'}
	# stack (list) to hold the last bracket that was open - when we come across
	# a closing bracket, it MUST correspond with the most recently opend bracket
    last_open = []
	# loop over chars in s
    for char in s:
		# if bracket is not in dict keys, it must be an opening bracket - add to stack
        if char not in pairs:
            last_open.append(char)
        else:
			# if we do not have any opening brackets remaining, or we have a mismatch 
			# (doesn't match corresponding value in dictionary), return False
            if not last_open or last_open[-1] != pairs[char]:
                return False
			# else, we have a match! pop last open off of end of stack before moving onto the next check
            last_open.pop()
	# make sure there are no remaining unclosed pairs in our list if we make it to the end
    return len(last_open) == 0