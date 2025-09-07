'''
this function takes two strings as input and returns the number of common characters between them.
'''
def countOfCommonCharacters(s1,s2):
    x = set(s1)
    y = set(s2)
    z = x.intersection(y)
    return len(z)

print(countOfCommonCharacters('kotlin','python'))
print(countOfCommonCharacters('noon','afternoon'))