def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    s = pattern
    t = str.split()
    return map(s.find, s) == map(t.index, t)


pattern = "abba"
str = "dog cat cat dog"
print(wordPattern(pattern, str))
