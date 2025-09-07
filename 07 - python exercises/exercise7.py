'''
this program generates a random string of 50 characters and then sorts it in reverse order
'''
from random import randint   

lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
       'p','q','r','s','t','u','v','w','x','y','z']

lst2 = [lst[randint(0,25)] for _ in range(50)]
    
lst2.sort(reverse=True)

s = ''.join(lst2)

print(s)    