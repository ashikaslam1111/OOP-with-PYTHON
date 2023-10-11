class Restrurent:
    def __init__(self,name) -> None:
         self.manger = []
         self.chef = []
         self.w8er=[]
         self.name = name
         self.item = {}
    def add_item(self,name,price):
         self.item[name]=price
    def add_manger(self,person):
         if len(self.manger)>0:
              print("we already have a manger so no need another one")
         else : self.manger.append(person)
    def add_chef(self,person):self.chef.append(person)
    def add_w8er(self,person):self.w8er.append(person)

    def see_all_man_power(self):
        for i in self.manger:print(i)
        for i in self.chef:print(i)
        for i in self.w8er:print(i)
    
class People:
     def __init__(self,name) -> None:
          self.name = name

class Maneger(People):
     def __init__(self, name,email,mobile,nid) -> None:
          super().__init__(name)
          self.name = name
          self.phn = mobile
          self.email = email
          self.nid = nid
     def __repr__(self) -> str:
           return f"Name = {self.name} nid = {self.nid} phn = {self.phn} email = {self.email} posisson = manager"
      
class Chef(People):
      def __init__(self, name,email,mobile,nid) -> None:
          super().__init__(name)
          self.name = name
          self.phn = mobile
          self.email = email
          self.nid = nid
      def __repr__(self) -> str:
           return f"Name = {self.name} nid = {self.nid} phn = {self.phn} email = {self.email} posisson = chef"
      

class Weater(People):
      def __init__(self, name,email,mobile,nid) -> None:
          super().__init__(name)
          self.name = name
          self.phn = mobile
          self.email = email
          self.nid = nid
      def __repr__(self) -> str:
           return f"Name = {self.name} nid = {self.nid} phn = {self.phn} email = {self.email} posisson = weater"
      

     
class Customer(People):
    def __init__(self, name) -> None:
         super().__init__(name)

     
    def make_order(self,item_name,company):
         if item_name in company.item:
              print('price is',company.item[item_name])
         else :print("sorry we don't have this item" )
         










# inter_action_testing

Dhal_Vath = Restrurent("Dhal_Vath")
Manegerx = Maneger('Monir',"hollo@111","017****",11234)
w81 = Weater('Monir1',"hollo@1112","017****1",112342)
w82 = Weater('Monir12',"hollo@11123","017****11",1123423)
chef1 = Chef('Monir12',"hollo@11123","017****11",1123423)
chef2 = Chef('Monir123',"hollo@111233","017****113",1123423)
Dhal_Vath.add_manger(Manegerx)
Dhal_Vath.add_chef(chef1)
Dhal_Vath.add_chef(chef2)
Dhal_Vath.add_w8er(w81)
Dhal_Vath.add_w8er(w82)

Dhal_Vath.see_all_man_power()
Manegery = Maneger('Monir',"hollo@111","017****",11234)
Dhal_Vath.add_manger(Manegery)

Dhal_Vath.add_item('khichuri',30)
Dhal_Vath.add_item('omlat',20)
print(Dhal_Vath.item)




byer1 = Customer("aslam")
byer1.make_order("khichuri",Dhal_Vath)