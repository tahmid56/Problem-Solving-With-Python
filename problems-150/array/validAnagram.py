def validAnagram(s, t):
    if len(s) != len(t):
        return False
    sDict, tDict = {}, {}

    for i in range(len(s)):
        sDict[s[i]] = 1 + sDict.get(s[i], 0)
        tDict[t[i]] = 1 + tDict.get(t[i], 0)

    for j in sDict:
        if sDict[j] != tDict.get(j, 0):
            return False

    return True


print(validAnagram("apaa", "paa"))
