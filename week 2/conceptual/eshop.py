
class Product:
   def __init__(self,name,price,quantity) -> None:
       self.name =name
       self.price = price
       self.quantity =quantity
       
class Store:
    def __init__(self) -> None:
        self.__product_price = {}
        self.__product_quantity ={}
        self._Name = 'aslam'
        self.__profit=0
    def profiT(self):return self.__profit
    def add_product(self,name,price,quantity):
        ProducT = Product(name,price,quantity)# here i made a object of product class
        self.__product_price[ProducT.name]=ProducT.price
        self.__product_quantity[ProducT.name]=ProducT.quantity
    def showPro(self):
       print("product are>>>")
       print(self.__product_price)
       print(self.__product_quantity)
    def buy_product(self,name,quantitY):
        if  name in self.__product_quantity:
            if self.__product_quantity[name]>=quantitY:
                self.__product_quantity[name]-=quantitY
                self.__profit+=(self.__product_price[name])*(.05)*quantitY
                print("thank you")
            else:print(f"sorry we have only {self.__product_quantity[name]}")
        else:print("unavailable")


class Shop(Store):
   def __init__(self,name):
       self.name =name
       super().__init__()
   def naME(self):
      return(self._Name)
       
   
#  .... main function>>>>>>      


Shop1 = Shop('applebd')
Shop1.add_product('iphon',120000,10)
Shop1.add_product('samsung s8',10000,10)
Shop1.showPro()
Shop1.buy_product('samsung s8',1)
Shop1.showPro()
print(Shop1.profiT())
       

