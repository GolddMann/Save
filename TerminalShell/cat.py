import sys
import keyword
from config.theme import color_scheme

if(len(sys.argv) < 2):
    print("Usage: cat file_name")
else:
    f = open(sys.argv[1], "r")
    data = f.read()
    keyword_list = keyword.kwlist
    for line in data.split('\n'):
        words = line.split(' ')
        for word in words:
            if(word in keyword_list):
                print(color_scheme["code"], end=f"{word} ")
            else:
                print("\x1b[37m", end=f"{word} ")
        print("")
    f.close()