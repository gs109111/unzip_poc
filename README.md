# unzip_poc
A proof-of-concept demonstrating how to view the structure of a ZIP archive (file/folder names) without knowing the password

This project shows how to extract:
* File names
* Directory hierarchy

All without decrypting or accessing protected file contents

# Example

Command:
python3 unzip_poc.py example.zip

Sample output:

Locked.zip
--> Documents/<space><space>
----> report.pdf<space><space>
----> notes.txt<space><space>
--> Images/<space><space>
----> photo.jpg<space><space>

No password is required to view the structure but contents remain blank

# Tested on
MacOS Tahoe 

# Disclaimer
- This tool is for research and educational purposes only
- It does not bypass encryption or access protected contents
- Use only on archives you own or have permission to analyze
