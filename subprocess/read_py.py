import subprocess
import sys
import os

file = sys.argv[1]

if os.path.exists(file):
    if os.path.isfile(file):
        result = subprocess.run(["python3", file], capture_output=True, text=True)
        print(result.stdout)

        result = subprocess.run(["python3", "-c", "print([i for i in range(50)])"],capture_output=True, text=True)
        print(result.stdout)
    else:
        print("Invalid file")

