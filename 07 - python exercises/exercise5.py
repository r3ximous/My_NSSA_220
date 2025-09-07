'''
this is a list comprehension exercise where we have to create 3 lists using list comprehension which are:
1. lst1: a list of even numbers from 0 to 100
2. lst2: a list of odd numbers from 1 to 101
3. lst3: a list of numbers which are the sum of the corresponding elements of lst1 and lst2
'''
lst1 = [2*i for i in range(50)]
lst2 = [2*i+1 for i in range(50)]
lst3 = [lst1[i] + lst2[i] for i in range(50)]
print(lst1)
print(lst2)
print(lst3)