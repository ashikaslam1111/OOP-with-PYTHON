class exam:
   def __init__(self,student,bangla,math,english):
      if bangla<=100 and bangla>=0 and english<=100 and english>=0 and math<=100 and math>=0:
       self.student=student
       self.bangla=bangla
       self.math=math
       self.english=english
       self.ave= (bangla+english+math)//3
   def   getGpa(self):
      if self.ave<33:
         return "F"
      elif  self.ave <41:
         return "D"
      elif  self.ave <51:
         return "C"
      elif  self.ave <61:
         return "B"
      elif  self.ave <71:
         return "B+"
      elif  self.ave <81:
         return "A"
      else:
         return 'A+'   
student1=exam('aslam',70,90,75)
print(student1.getGpa())