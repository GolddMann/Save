import os
import config.theme as theme

def unknown(com):
    print("Unknown command: " + com)

class Path(object):
    def __init__(self, curr_path):
        self.curr_path = curr_path
        self.base_path = "C:\\Users\\Stark\\Desktop\\programs\\myown\\TerminalShell\\"
    
    def change_path(self, new_path):
        self.curr_path = new_path
    
    def get_curr(self):
        return self.curr_path
    
    def get_base(self):
        return self.base_path


path = Path(os.getcwd() + '\\')

def main():
    
    hf = open(path.get_base() + "history", "a+")

    while True:
        shell_theme = theme.color_scheme["shell"]
        print(f"{shell_theme}$pyshell>: ", end="")
        command_full = input("")

        command, *arguments = command_full.split(" ")

        hf.write(command_full + "\n")

        if(command == "exit"):
            break


        if(not os.path.exists(path.get_base() + command + '.py')):
            if(not os.path.exists(path.get_curr() + command + '.py')):
                os.system(f"{command} " + " ".join(arguments))
                continue
            else:
                os.system(f"python {path.get_curr() + command}.py " + " ".join(arguments))
        else:
            os.system(f"python {path.get_base() + command}.py " + " ".join(arguments))
        
        print(path.get_curr())
            

    hf.close()


if __name__ == "__main__":
    main()
