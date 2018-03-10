import collections


def canConstruct(ransomNote, magazine):
    a = collections.Counter(ransomNote)
    b = collections.Counter(magazine)
    return a - b

ransomNote = "aabbc"
magazine = "aaab"
print(canConstruct(ransomNote, magazine))
