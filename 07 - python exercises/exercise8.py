'''
this script takes a directory as an argument and prints the number of files in it
'''
import sys
import os

path = sys.argv[1]

if os.path.isdir(path):
    print(len(os.listdir(path)))
else:
    print('Not a directory')    