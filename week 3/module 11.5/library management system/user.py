from collections import deque


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.history = deque()
        self.iD = None
        self.password = None
        self.email = None

    def register(self, library):
        if self.iD != None:
            print("you are alreay a user>")
            flag = None
            print("to see history prees 1")
            print("to return book prees 2")
            print("to borrow book prees 3")
            print("to exit prees any button")
            flag =int(input("enter ur choice>>"))
            if flag == 1: self.see_history()
            elif flag == 2: self.return_book(library)
            elif flag == 3: self.borrow_book(library)
            else:
                print("heave a good day ")
                return ""
        else:
            self.email = input("enter your email>>")
            self.password = input("enter your password>>")
            library.resgister(self.email, self.password, self)

            flag = None
            print("to see history prees 1")
            print("to return book prees 2")
            print("to borrow book prees 3")
            print("to exit prees any button")

            flag =int(input("enter ur choice>>"))
            if flag == 1: self.see_history()
            elif flag == 2: self.return_book(library)
            elif flag == 3: self.borrow_book(library)
            
            else:
                print("heave a good day ")
                return ""




        def loging(self, library):
             if self.iD == None:
               print("you are not registered so register first>")
               self.register(library)
             else:
              flag = None
              print("to see history prees 1")
              print("to return book prees 2")
              print("to borrow book prees 3")
              print("to exit prees any button")
              if flag == 1: self.see_history()
              elif flag == 2: self.return_book()
              elif flag == 2: self.borrow_book()
              else:
                print("heave a good day ")
                return ""










    def  borrow_book(self,library):
       
       library.borrow_request(self)

    def return_book(self,library):
       library.return_request(self)

    def see_history(self):
        for i in self.history:
           print(i)