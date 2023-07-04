

class phone:
    def __init__(self,price,brand,woner):# it works like constructor and so when i  will creat a data fo this class i have to give all the paramiter as i initialize in this consturctor 
         #pass  if we do not do anythin in this constructor then we have to write psss
         self.price=price
         self.brand=brand
         self.woner=woner
         
        
    made_in="china"
    def call(self,name):
        sms = f"hell {name} it is china"
        print(sms)
      

a = phone(1000,'sum','alam')
print(a.woner)


## init is nothing but constructor


