# Modules
import os
import sys

# Initial Variables
print("")

zip_file = sys.argv[1]
zip_file_size = int(os.popen(f"unzip -l {zip_file} | wc -l").read().strip().replace("\n", ""))
os.system("clear")

print("")

print(f"Cracking Structure...")

def flood(line):
    os.system(f"unzip -o -P {line} {zip_file} &>/dev/null")

for num in range(1, zip_file_size ** 2):
    flood(num)

print("")
