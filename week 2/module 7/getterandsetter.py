class person:
    def __init__(self,age) -> None:
        self.__age=age
    
    @property
    def getAge(self):
        return self.__age
    @getAge.setter
    def setAge(self,value):
        self.__age+=value

    











monir = person(18)
monir.setAge=2
print(monir.getAge)