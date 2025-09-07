'''
this code will take a string as input and return the number of words and characters in the string
'''
def analyzeString(s):
    w = len(s.strip().split(' '))
    c = len(s.replace(' ', ''))   
    return w,c

print(analyzeString('welcome'))
print(analyzeString('welcome to python'))