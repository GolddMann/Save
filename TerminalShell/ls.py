import os
import sys
import random
import ansicon

colors = {
    "Red": "\x1b[31m",
    "Green": "\x1b[32m",
    "Yellow": "\x1b[33m",
    "Blue": "\x1b[34m",
    "Magenta": "\x1b[35m",
    "Cyan": "\x1b[36m",
    "White": "\x1b[37m"
}


def get_size_mesuare(size):
    mesuares = {
        0: 'Bytes',
        1: 'KBytes',
        2: 'MBytes',
        3: 'GBytes',
        4: 'TBytes'
    }
    i = 0
    while(size >= 1024 and i < 4):
        size /= 1024.
        i += 1

    return "{:.2f} {}".format(size, mesuares[i])


if not ansicon.loaded():
    ansicon.load()

files = os.listdir(sys.path[0])

max_len = 0
tab_size = 8

for i in range(len(files)):
    max_len = max(len(files[i]), max_len)

for i in range(len(files)):
    if(not os.path.isfile(files[i])):
        continue
    color_num = random.randint(0, 6)
    print(colors[list(colors.keys())[color_num]], end="")
    file = open(files[i], "a")
    size = file.tell()
    tabs = "\t"*((max_len - len(files[i]))//tab_size + 1)
    size_mesuare = get_size_mesuare(size)
    print(f"{i+1}: {files[i]}{tabs}{size_mesuare}")


if ansicon.loaded():
    ansicon.unload()