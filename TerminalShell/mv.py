import shutil
import os
import sys

if(len(sys.argv) < 3):
    print("Usage of mv command: mv file_path1 file_path2")
else:
    shutil.move(
        os.getcwd() + f"\{sys.argv[1]}", os.getcwd() + f"\{sys.argv[2]}")
