from requests import get
from zipfile import ZipFile
from io import BytesIO
from os import path, system, chdir, getcwd
class main:
    def __init__(self,moduleDir,startDir,pluginsFolder) -> None:
        self.moduleDir = moduleDir

    def kiddionsmenu(self,cmd:str):
        KIDDIONS = "modest-menu_v0.9.6"
        if path.exists(f"{self.moduleDir}\\{KIDDIONS}"):
            dir_before_changing_to_kiddions = getcwd()
            chdir(f"{self.moduleDir}\\{KIDDIONS}")
            system("modest-menu.exe")
            chdir(dir_before_changing_to_kiddions)
        else:
            print("Kiddions Folder doesn't exist! Please reinstall kiddionsmodmenu for PyPlConsole!")
        

    