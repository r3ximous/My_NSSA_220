import subprocess

result = subprocess.run(["bash","loop.sh", "5"],capture_output=True, text=True)

print(result.stdout)
print(result.stderr)
print(result.returncode)