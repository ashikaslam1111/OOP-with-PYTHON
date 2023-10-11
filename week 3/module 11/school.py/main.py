from school import*
from person import*



def main():
    school1 = School('tpi','tangail')
    eight = Classroom('eight')
    school1.add_calssroom(eight)
    nine = Classroom('nine')
    school1.add_calssroom(nine)
    print(school1)

    abul = Student('dhian',eight)
    school1.studens_addmition(abul)
    babul = Student('dhian1',eight)
    school1.studens_addmition(babul)

    print(school1)

    # subject 
    teacher = Teacher('monir')
    bangle = Subject('bangle', teacher)
    teacher1 = Teacher('monir1')
    bangle1 = Subject('bangle1', teacher1)

    eight.add_subject(bangle)
    eight.add_subject(bangle1)
    
    print(school1)
    eight.semester_final()
    print(school1)







if __name__ == "__main__":main()