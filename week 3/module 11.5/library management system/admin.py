


class Admin:
    def __init__(self,name,email) -> None:
        self.name = name
        self.email = email
        self.password = None



    def add_book(self):
        name = input("inter name of the book>>")
        cata = input("inter catagiry of the book>>")
        cout = input("how many book you wanna add>>")
        