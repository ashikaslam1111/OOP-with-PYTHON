
class student:
    def __init__(self,name,id,Class):
        self.Class=Class
        self.name=name
        self.roll = id     

    def __repr__(self):
        return f"a student with name {self.name} currently is in class {self.Class} roll is {self.roll}"
    


sutuendt1 = student('aslam',570963,'cse 5th semester')
print(sutuendt1)

         