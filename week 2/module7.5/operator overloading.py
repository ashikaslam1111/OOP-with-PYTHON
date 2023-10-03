

class person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age =age

    def __add__(self,other):
        return self.age + other.age
    

person1 = person('monir',27)
person2 = person('pappu',33)
print(person1+person2)