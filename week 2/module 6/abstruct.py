from abc import ABC,abstractmethod

#  abs = abstract base class

class animal(ABC):
    @abstractmethod  # it will inforces all child class to have eat() function
    def eat(self):
       pass
    def move(self):
        pass


class monky(animal):
    def __init__(self,name) -> None:
        self.Name = name
        super().__init__()
    def eat(self):
         print(f"ola im eating bannana!!")



monky1 = monky('ben')
monky1.eat()

