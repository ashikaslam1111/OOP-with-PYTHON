
from typing import Any
class shop:
    product = {1:("alo",15),2:('begun',20),3:("potol",30),4:("sosa",20),5:("morich",40),6:("tometo",10)}
    def __init__(self) -> None:
        self.costomer_name='x'
        self.chart=[]
        self.total = 0
        self.given=0
        self.returned=0
        self.more_mony=0


    def buy_sometin(self):#........................................functon for buy element 
        self.costomer_name=input("please enter your name>>")
        flag = 0
        flag = int(input("if you wanna take some thing pres 1 else 0>>"))
        if flag==1:
            print(".....here is our all product and price list.....")
            for key,valu in self.product.items():
                print(f"{key}: {valu[0]} is {valu[1]}tk per kg")
            flag2=1
            iteN=0
            amo =0
            while 1:
                iteN=0
                amo=0
                flag2 = int(input("for checking out prees 0 else 1>>"))
                if flag2 ==1:
                      iteN=int(input("input the item number>>"))
                      amo=int(input("how many kg you wanna buy?>>"))
                      self.total+=self.product[iteN][1]*amo
                      self.chart.append([iteN,amo])
                else :break
            self.check_out()
        else: self.check_out()


    def remove_from_cart(self):#........................................functon for remove element 
              print(".....your chart is......")
              for index,value in enumerate( self.chart):   
                  i = index+1
                  kg = value[1]
                  it = value[0]
                  itN = self.product[it][0]
                  pr = self.product[it][1]
                  print(f"{i}: {itN} {kg} kg per kg is {pr} tk")
              flag4 =1
              while flag4==1:
                 rit=int(input("inter the item number that you wanna remove>>"))
                 rkg=int(input("how meny kg you wanna remove>>"))
                 indofmp= self.chart[rit-1][0]
                 itpr =  self.product[indofmp][1]
                 gotkg = self.chart[rit-1][1]
                 if(gotkg>=rkg):self.total-=itpr*rkg
                 else :self.total-=itpr*gotkg
                 self.chart[rit-1][1]-=rkg
                 if self.chart[rit-1][1]<=0:
                     del self.chart[rit-1]
                 flag4 = int(input("if you wanna remove more then pres 1 or for chackput press 0>>"))
              self.check_out()



    def check_out(self):#........................................functon for chack out
       if self.total==0:print("THANK YOU FOR VISITING US HOPE YOU WILL COME BACK AGIN")
       else :
           print("you have bought....")
           for i in self.chart:
               am = i[1]
               N = i[0]
               tk = self.product[N][1]
               it = self.product[N][0]
               print(f"you have boutht {it} {am} kg cost {tk*am}")
           print()
           print(f"you have buy in  total {self.total} tk")
           print(f"given mony is {self.given} tk")   

           if(self.given<self.total):
                 print(f"you have to pay in  total {self.total -self.given} tk")
                 pay1 =int(input("pleae give us the money>>"))
                 self.given+=pay1

           if(self.given>=self.total):
               print(f"""
               .....here is your RECEIPT sir.....
               costomer name: {self.costomer_name}
               total={self.total}
               given={self.given}
               returned = {self.given - self.total}
               """)
           else:
                while self.given<self.total:
                   need = self.total-self.given
                   pay_again=0
                   print(f"sorry sir you have to pay {need} more ")
                   flag3=0
                   flag3=int(input(f"for removing some item from your chart press 0 or if you wanna pay the money press 1>>"))
                   if(flag3 == 1):
                         pay_again=int(input("pleae give us the money>>"))
                         self.given+=pay_again
                   else :
                       self. remove_from_cart()
                if(self.given>=self.total):
                  print(f"""
               .....here is your RECEIPT sir.....
               costomer name: {self.costomer_name}
               total={self.total}
               given={self.given}
               returned = {self.given - self.total}
               """)   
                
# main>>>>>>>>>>>
person1 = shop()
person1.buy_sometin()


