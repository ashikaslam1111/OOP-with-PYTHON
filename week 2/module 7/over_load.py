class person:
    def __init__(self,age,height) :
        self.Age = age
        self.Height = height

class my_friend(person):
    def __init__(self,name, age, height):
        self.Name = name
        super().__init__(age, height)
    def __add__(self,other):
        return self.Age + other.Age
    
    def __gt__(self,other):
        return self.Age>other.Age





# main()..........

monir = my_friend('dihan',19,60)
pappu = my_friend('sagol',18,65)

print(monir+pappu)
print(monir>pappu)