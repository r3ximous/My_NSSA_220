def analyzeString(s):
    words = s.split()
    num_words = len(words)
    num_chars = sum(len(word) for word in words)
    return num_words, num_chars

# Example usage:
# result = analyzeString("welcome to python")
# print(result)  # Output: (3, 15)

def AnalyzeSting(s):
    countOfWords = len(s.replace(' ', ''))

def count_unique_com_char(s1,s2):
    # doc string
    """
    x = set()
    for c1,c2 in s1,s2:
        for c2 in s2:
            if c1 == c2:
                x.add(c1) 
    """
    s1 = set(s1)
    s2 = set(s2)
    x = s1.intersection(s2)

    return len(x)

s = "welcome to python"
print(count_unique_com_char(s, "hello world"))  # Output: 4

print(analyzeString(s))
print(AnalyzeSting(s))