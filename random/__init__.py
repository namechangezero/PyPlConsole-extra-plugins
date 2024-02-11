import random
class main:
    def __init__(self, moduleDir, startDir,*a) -> None:
        pass
    
    def random(self, cmd:str):
        length_ = int(cmd.split(" ")[1])
        _s = "abcdefghijklmnopqrstuvwxyz"
        _s += _s.upper() + "0123456789"
        r_ = "".join(_s[random.randint(0,len(_s)-1)] for i in range(length_))
        print(r_)


        

