class user:
    def __init__(self,name,age,slary) -> None:
        self.__name = name
        self__age=age
        self.__salary=slary
    
    @property # and the function will work like a atribute or variale so i can not call  it like like a function 
    def get_salary(self):# it is a getter 
       return self.__salary #getter without any setter is read only

    @get_salary.setter
    def set_salary(self,amount):
        self.__salary+=amount



person1=user('smasu',21,1200)
person1.set_salary = 300
print(person1.get_salary)
