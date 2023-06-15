import subprocess
import re
import time


print("[+] Please wait, Compiling the file to EXE ...")
subprocess.call("pyinstaller --onefile main.py", shell=True)

