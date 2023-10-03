from abc import ABC,abstractmethod

class stuednt(ABC):
    @abstractmethod
    def gender(self):
        pass

class boy(stuednt):
    def gender(self):
       print("im a boy")

class girl(stuednt):
    def gender(self):
        print("im a girl")

g1=boy()
g1.gender()