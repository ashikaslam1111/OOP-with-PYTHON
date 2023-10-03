
from typing import Any


class person:
    def __init__(self,name,height,weight,genger):
        self.Name = name
        self.Height=height
        self.Weight=weight
        self.Gender=genger
    def eat(self):
        print("vat ,dal,mangso etc")
    def exersige():
        raise NotImplementedError
    


class genrelperson(person):
    def __init__(self, name, height, weight, genger):
        super().__init__(name, height, weight, genger)

    def exersige(self):
       print("no need to exersige ha ha....")


class cricketer(person):
    def __init__(self, name, height, weight, genger,team):
        self.Team = team
        super().__init__(name, height, weight, genger)
    
    def eat(self):
        print('we eat only vigitable to keep our body fit')

    def exersige(self):
        print("we must go to gym")




# main........

monir = genrelperson('dihan',60,56,'male')

monir.eat()
monir.exersige()



shakib = cricketer('shakim',69,60,'male','bd')

shakib.eat()
shakib.exersige()
    
        











