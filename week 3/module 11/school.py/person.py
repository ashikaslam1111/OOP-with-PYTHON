import random

class Person:
    def __init__(self,name) -> None:
       self.name = name



class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
       

    def teach(self):
        pass

    def evaluat_exam(self):
           marks = random.randint(0,100)
           return marks
       
    
    def __repr__(self) -> str:
        return f'name is {self.name}  '

class Student(Person):
    def __init__(self, name,class_room) -> None:
        super().__init__(name)
        self.__id = None
        self.classroom =class_room
        self.marks ={}
        self.gread =None
  

    @property
    def id_(self):
        return self.__id
    @id_.setter
    def id_set(self,value):
        self.__id = value


