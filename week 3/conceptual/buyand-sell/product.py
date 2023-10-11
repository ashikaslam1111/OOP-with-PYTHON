class Product:
    def __init__(self,ctagory,name,price) -> None:
         self.catogry = ctagory
         self.name  = name 
         self.price = price

    def __repr__(self) -> str:
         return f"""
Name is {self.name}
Catagory is { self.catogry}
Price is {self.price}
         """