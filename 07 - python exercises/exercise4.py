'''
this program generates 3 random numbers and prints the maximum one using randrange and randint
'''
from random import randrange
from random import randint

x,y,z = randrange(100), randrange(100), randrange(100)
print('random numbers:',x,y,z)
print('max is', max(x,y,z))

a,b,c = randint(1,100), randint(1,200), randint(1,200)
print('random numbers:',a,b,c)
print('max is', max(a,b,c))