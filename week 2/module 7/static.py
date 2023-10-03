class shop:
    chart = [] # it is a static atribute cz it is common for every one
    coutry = "china"  # it also static
    def __init__(self,name,location) -> None:
       self.Name = name
       self.Locatin = location # thise are instance atribute 

    # there can be static method 
    @classmethod # it cna  work with instance atibute 
    def purchase(self,item,price,amount):
          remaining  =  amount - price
          print(f'buying {item} for price and remaining {remaining}')
    @staticmethod  # it cna not work with instance atibute 
    def mul(a,b):
        print(a*b)







shop.purchase('lungi',200,300)
shop.mul(3,5)