# Given a string s, find the first non-repeating character in it 
# and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "codingtemple"
# Output: 0
# Example 2:
# Input: s = "codingcodingalumni"
# Output: 12
# Example 3:
# Input: s = "ctct"
# Output: -1

# Marquese Brown Solution

def non_repeat_v2(s):
    lst = []
    bad = []
    for i, v in enumerate(s):
        if v not in lst and v not in bad:
            lst.append(v)
        elif v in bad:
            continue
        else:
            bad.append(v)
            lst.remove(v)
    return s.index(lst[0]) if lst else -1 

# Ben Peterson Solution

def non_repeat(string):
    for i in range(len(string)):
        if string[i] not in string[i+1:] and string[i] not in string[:i]:
            return i
    return -1


print(non_repeat('codingtemple'))
print(non_repeat("codingcodingalumni"))
print(non_repeat("ctct"))

# Jon Watts Solution

def nonRepeatingLetter2(s):
    letterDict = {}
    letterLoc = {}
    for i in range(len(s)):
        if s[i] not in letterLoc:
            letterLoc[s[i]] = i
            letterDict[s[i]] = 1
        else:
            letterDict[s[i]] = letterDict.get(s[i]) + 1
    if min(letterDict.items())[-1] == 1:
        return min(letterLoc.items())[-1]
    else:
        return -1