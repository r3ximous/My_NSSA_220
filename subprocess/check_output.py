import subprocess

output = subprocess.check_output(["python3","--version"], text=True)

print(output)