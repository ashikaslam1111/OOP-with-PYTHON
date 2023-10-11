
class Product:
    def __init__(self,name,price) -> None:
        self.Name = name
        self.Price =price




pro1 = Product('ipn',100)

print(pro1)
print(vars(pro1))
a=vars(pro1)
print(type(a))