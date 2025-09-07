'''
this script should take a path as an argument and print out whether the path is a file or a directory.
'''
import sys
import os

path = sys.argv[1]
if os.path.exists(path):
    if os.path.isdir(path):
        print('Direcotry')
    elif os.path.isfile(path):
        print('File')    
else:
    print('Invalid')    