class pen:
    def __init__(self,name,price,color) :
        self.name=name
        self.color=color
        self.price=price
        self.discount_price= price - price*(5/100)


pen1=pen('matador all time',6,'green')   
print(pen1.discount_price)    
        