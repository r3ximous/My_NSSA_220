import subprocess

result = subprocess.run(["pwd"], capture_output=True, text=True)

print("output: ",result.stdout)
if result.returncode != 0:
    print("error: ",result.stderr)