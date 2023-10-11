class Book:
    def __init__(self,name,ctagory) -> None:
        self.name = name
        self.catagory = ctagory

    def __repr__(self) -> str:
       return f"name is {self.name}  catagory is {self.catagory}"



