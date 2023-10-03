

class shape:
    def __init__(self,name) -> None:
        self.Name = name
    def area(self):
        pass

class triangle(shape):
    def __init__(self, name,base,height) -> None:
        self.b=base
        self.h=height
        super().__init__(name)
    def area(self):
        print(f"the area of {self.Name} is {.5*self.b*self.h}")


class squer(shape):
    def __init__(self, name,base) -> None:
        self.b=base
        super().__init__(name)
    def area(self):
        print(f"the area of {self.Name} is {self.b**2}")























#.....................MAIN..................................


tri1 = triangle('tribuj1',2,3)
tri1.area()
borgo1=squer('borgo',3)
borgo1.area()


print(issubclass(squer,shape))

print(isinstance(tri1,shape))

