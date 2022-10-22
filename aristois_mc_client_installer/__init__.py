from platform import system
from subprocess import check_output, run, STDOUT
from webbrowser import open as open_browser
from requests import get
from os import getcwd, remove, path
class main:
    was_run = False
    def __init__(self, pluginDir, startDir) -> None:
        self.download_url_aristois="https://gitlab.com/Aristois/ui-installer/-/jobs/2505715157/artifacts/raw/packager/Aristois-Free.jar"
        self.dir = getcwd()

    def aristois_install(self,cmd):
        if system()!="Windows":
            print("Only availible for Windows. Linux and MacOS coming in future!")
            return

        if not check_output(["java","-version"],stderr=STDOUT,shell=True).startswith(b"java"):
            print("Please install Java first, and then install again")
            download_link_java = "https://www.java.com/de/download/"
            open_browser(download_link_java)
            return

        self.filename = "Aristois_installer.jar"
        response = get(self.download_url_aristois)
        with open(self.filename,"wb") as f:
            f.write(response.content)
        
        self.was_run = True
        
        run(["java","-jar",self.filename])

        

    def _bye(self):
        if self.was_run:
            jarPath = self.dir+"/"+self.filename
            if path.exists(jarPath):
                remove(self.dir+"/"+self.filename)

