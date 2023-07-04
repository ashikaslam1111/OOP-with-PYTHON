

class shoping:
    def __init__(self,name):
        self.name = name
        self.cart = []
        self.total_amount =0

    def add_to_cart(self,item,price,quantity):
        product = {'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)
    def total(self):
        to = 0
        for i in self.cart:
            to+=i['price']*i['quantity']
        self.total_amount =to    
    def chekcout(self,cash):
       self.total()
       if self.total_amount>cash:
           print(f'your total cost is {self.total_amount} plsese pay  {self.total_amount - cash}')

    def removeE_Item(self,item):
        for i in self.cart:
            for key,valu in i.items():
                if item == valu:
                   self.cart.remove(i)

person1 = shoping('aslam')
person1.add_to_cart('book',100,4)
person1.add_to_cart('pen',100,3)
person1.chekcout(200)
person1.removeE_Item('book')
print(person1.cart)











