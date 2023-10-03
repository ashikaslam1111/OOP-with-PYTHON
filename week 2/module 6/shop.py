class shop:
    def __init__(self,name) -> None:
       self. cart = []
       self.allcost=0
    def bye(self,item,price):
            now = {item:price}
            self.cart.append(now)
            self.allcost+=price
    def total(self):
         return f"you have to pay tk{self.allcost}"
         
            
        


# mian....................
person1 = shop("Aslam")
person1.bye('cola',100)


print(person1.total())




