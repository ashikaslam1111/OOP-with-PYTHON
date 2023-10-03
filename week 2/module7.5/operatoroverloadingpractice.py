 
class player:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def __gt__(self,other):
        return self.age>other.age\
        

shakib = player('shakib',35)
mushfiq = player('mushi',38)

print(shakib>mushfiq)      