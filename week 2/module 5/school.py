class student:
    def __init__(self,name,current_class,id):
        self.name = name
        self.roll=id
        self.Class=current_class
    def __repr__(self):
        return f""" 
        stuent name is {self.name} 
        class is {self.Class}
        id is {self.roll}
                 """
    
class teacher:
    def __init__(self,name,sub,id):
        self.Name=name
        self.subject =sub
        self.Id=id
    def __repr__(self):
        return f"""
        teacher name is {self.Name}
        subject is {self.subject}
        id is {self.Id}
        """
    
class school:
    def __init__(self,name):
        self.Name = name
        self.teachers =[]
        self.students=[]

    def add_teachr(self,name,sub):
        id = len(self.teachers)+101
        TeacheR = teacher(name,sub,id)
        self.teachers.append(TeacheR)
    
    def enroll(self,name,fee):
        if(fee<6500):
            return f" not enough fee need {6500-fee} more!!!"
        else :
            id = len(self.students)+1
            stu = student(name,'C',id)
            self.students.append(stu)

    def information(self):
        print(f"well come to {self.Name} ")
        print("...........our teachers are............")
        for i in self.teachers:print(i)
        print("...........our students are............")
        for i in self.students:print(i)

# now this is the part of main function

phitron = school("PHITRON")

phitron.enroll('ashik',4000)
phitron.enroll('monin',40000)
phitron.add_teachr('golam',"algo")




phitron.information()

        

    











