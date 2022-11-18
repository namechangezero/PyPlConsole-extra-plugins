from os import listdir, path
from colorama import init as init_colorama, Fore
class main:
    def __init__(self, moduleDir, startDir) -> None:
        init_colorama()

    def oncmd(self, command):
        pass

    def onenter(self, command):
        pass

    def search(self, cmd:str):
        cmd = cmd.split()
        if len(cmd) < 2:
            print("You need to give 1 Argument.")
            return
        
        to_search = cmd[1]
        found_files = []

        for x in listdir():
            if to_search in x:
                found_files.append(x)

        print("""Results: 
--------""")
        if len(found_files) == 0:
            print("None")
            return

        for x in found_files:
            if path.isdir(x):
                print(f'{Fore.GREEN}{x}{Fore.RESET}', end="\n")
            else:
                print(f'{x}', end="\n")

        print("--------")
