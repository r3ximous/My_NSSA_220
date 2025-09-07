import subprocess

result = subprocess.run(["pwd"], capture_output=True, text=True)

print("output: ",result.stdout)
print("error: ",result.stderr)