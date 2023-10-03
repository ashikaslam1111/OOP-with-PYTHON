from abc import ABC,abstractmethod

class animal:
    def __init__(self,name) -> None:
        self.Name =name
    def __repr__(self) -> str:
        return f"im a {self.Name}"
    @abstractmethod
    def eat(self):
        pass
        

class cat(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    # def eat(self):
    #     print("i eat fish")
       


a1 = cat('pussy')
print(a1)