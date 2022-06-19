from sys import argv

hf = open("history", "a+")

if(len(argv) == 1):
    hf.seek(0)
    print(hf.read())
else:
    if(argv[1] == '-c'):
        hf.truncate(0)

hf.close()
