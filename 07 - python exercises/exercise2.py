'''
this program prints a triangle of stars with N rows
'''
N = input("Enter an integer: ")
N = int(N)

for i in range(N):
    for j in range(i+1):
        print('*', end = '')
    print()       

# Another solution    
for i in range(N):
    print('*' * i)