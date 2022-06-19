import sys
import os

if(len(sys.argv) < 3):
    print("Usage: copy src_file dst_file")
else:
    try:
        src_file = open(f"{os.getcwd()}\{sys.argv[1]}", "r")
        dst_file = open(f"{os.getcwd()}\{sys.argv[2]}", "w")
        dst_file.write(src_file.read())
        
    except:
        print("Unable to copy data!")