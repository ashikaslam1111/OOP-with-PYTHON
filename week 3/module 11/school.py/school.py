

class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        # composition
        self.classrooms = {}
    
    @staticmethod
    def gread_calculate(marks):
        n = len(marks)
        sum = 0
        for kye,vale in marks.items():
            sum+=vale
        av = int(sum/n)
        if av>=80 :return "A+"
        if av>=70 :return "A"
        if av>=60 :return "A-"
        if av>=50 :return "B"
        if av>=40 :return "B-"
        if av>=30 :return "C"
        return "F"




    def add_calssroom(self, classroom):
        self.classrooms[classroom.name] = classroom



    def studens_addmition(self, student):
        class_room = student.classroom 
        if class_room.name in self.classrooms:
            # TODO set student id
            self.classrooms[class_room.name].add_student(student)
        else:
            print("no class room for {class_room_name}")



    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    
    def __repr__(self) -> str:
        print("---------- all ----- classes")
        for key,value in self.classrooms.items():
            print(key)

        print("---------- students -------------")
        eight = self.classrooms["eight"]
        for i in eight.students:print(i.name)
        print("-------- subject and teachers----------")
        print(len(eight.sujects))
        for i in eight.sujects:
            print(i.name," ", i.teacher.name)
        
        print("---------- marks ar --------------")
        for stu in eight.students:
            print("...........")
            for key,value in stu.marks.items():
                print(key," ",value)
            print(stu.gread)
            print("...........")

        
        return ""


class Classroom:
    def __init__(self, name) -> None:
        self.name = name
        # composition
        self.students = []
        self.sujects =[]

    def add_student(self, student):
        serial_id = f"{self.name}-{ len(self.students)+1}"
        student.id_set =  serial_id
        student.classroom =self.name
        self.students.append(student)

    def __str__(self) -> str:
        return f"{self.name}  {len(self.students)}"

    def get_top_students(self):
        pass
        # sort student by gread


    def add_subject(self,sub):
        self.sujects.append(sub)


    def semester_final(self):
        for sub in self.sujects:
            sub.exam(self.students)

        for stu in self.students:
            gread = School.gread_calculate(stu.marks)
            stu.gread =  gread
        


        



class Subject:
    def __init__(self,name,teacher) -> None:
        self.name = name
        self.marks = 100
        self.pass_mark = 30
        self.teacher = teacher

    def exam(self,students):
       for stu in students:
           marks = self.teacher. evaluat_exam()
           stu.marks[self.name]=marks
           