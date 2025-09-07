import sys
import os

path = sys.argv[1]

if os.path.isdir(path):
    print(f"{path} is a directory")
elif os.path.isfile(path):
    print(f"{path} is a file")
else:
    print(f"{path} is something else")

# Run the script
# python demo.py /path/to/file