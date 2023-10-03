class cpu:
    def __init__(self,core) -> None:
        self.core = core
    
class ram:
    def __init__(self,size) -> None:
        self.ram = size

class ssd:
    def __init__(self,capacity) -> None:
        self.capa = capacity


class laptop:
    def __init__(self,pro,mamory,storage) -> None:
        self.prosesor = cpu(pro)
        self.RAm = ram(mamory)
        self.sto = ssd(storage)
        
mypc=  laptop(4,8,500)
print(mypc.RAm.ram)
        