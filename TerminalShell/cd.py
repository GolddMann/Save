import sys
import os
from shell import path

print(path)

if(len(sys.argv) < 2):
    print("Usage: cd dir_name")
else:
    folders = filter(os.path.isdir, os.listdir(path.get_curr()))
    if(sys.argv[1] not in folders):
        print("Unable to find path:", path.get_curr() + sys.argv[1])
        exit(0)
    path.change_path(path.get_curr() + sys.argv[1] + '\\')
    print("ok")
    