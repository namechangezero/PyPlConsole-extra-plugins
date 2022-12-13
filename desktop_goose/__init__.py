from os import path
from subprocess import Popen
class main:
    def __init__(self, moduleDir,startDir,*a) -> None:
        self.DEKSTOP_GOOSE_DIR = path.join(moduleDir, "DesktopGoose")
        self.GOOSE_EXECUTABLE = path.join(self.DEKSTOP_GOOSE_DIR, "GooseDesktop.exe")
    
    def oncmd(self, cmd) -> None:
        if cmd == "goose start":
            self._start_goose()
        elif cmd == "goose stop":
            self._stop_goose()
        
        return True

    def _start_goose(self) -> None:
        Popen([self.GOOSE_EXECUTABLE])

    def _stop_goose(self) -> None:
        Popen(["taskkill", "/f", "/im", "GooseDesktop.exe"])
    