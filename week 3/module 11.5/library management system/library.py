
from book import *
from recieve import*
from datetime import datetime




class Library:
    def __init__(self, name) -> None:
        ## book managemaet section---------
        self.books = {}
        self.total_catagory = 0
        self.total_books = 0
        self.cout_taker_of_any_book = {}

        ## lenden section---------



        ## user management section--------
        self.next_user_id = 1
        self.users ={  }




######## function for book managemaet

    def add_book(self, book, number): ## for the admin
        self.total_books += number
        if book.catagory in self.books:
            if book.name not in self.cout_taker_of_any_book:
                self.books[book.catagory].append(book)
        else:
            self.books[book.catagory] = [book]
        if book.name in self.cout_taker_of_any_book:
            self.cout_taker_of_any_book[book.name] += number
        else:
            self.cout_taker_of_any_book[book.name] = number

    def see_book(self):
        print("we have ", self.total_books, "book in total")
        for key, value in self.books.items():
            print("catagory is >>>>> ", key)
            for book in value:
                print(
                    f"book name is {book.name} available is {self.cout_taker_of_any_book[book.name]} piece")


    def remove_book(self,name,cata): ## for the admin
        if name in  self.cout_taker_of_any_book and self.cout_taker_of_any_book[name]>0:
           for i in  self.books[cata]:
               if i.name == name:
                    self.books[cata].remove(i)
                    self.total_books -= self.cout_taker_of_any_book[name]
                    self.cout_taker_of_any_book[name] = 0

                   
    def  borrow_request(self,user):
        print("hello1")
        if len(user.history)>0:
           if user.history[-1].returN_time==None:
               print('untill you do not return your priviou book you cna not borro a new book')
               flag = int(input("prees 1 for return book else any>>"))
               if flag == 1:
                  user.return_book(self)
                  print("-----see our books-----")
                  self.see_book()
                  bokname = input("enter the book name >>")
                  cata = input("enter the catagory name>>")
                  if bokname in  self.cout_taker_of_any_book and self.cout_taker_of_any_book[bokname]>0:
                      for book in self.books[cata]:
                          if book.name == bokname:
                              new_ricv = Recieve(user,book)
                              self.cout_taker_of_any_book[bokname]-=1
                              self.total_books-=1
                              user.history.append(new_ricv)
                              print("book brrow process done >>")
                              print(new_ricv)
                              return ""

                  else :
                      print("currently we dont have this book")
                      return ""
               else :
                   print("have a good day>>")
                   return ""
        else:


                  print("-----see our books-----")
                  self.see_book()
                  bokname = input("enter the book name >>")
                  cata = input("enter the catagory name>>")
                  if bokname in  self.cout_taker_of_any_book and self.cout_taker_of_any_book[bokname]>0:
                      for book in self.books[cata]:
                          if book.name == bokname:
                              new_ricv = Recieve(user,book)
                              self.cout_taker_of_any_book[bokname]-=1
                              self.total_books-=1
                              user.history.append(new_ricv)
                              print("book brrow process done >>")
                              print(new_ricv)
                              return ""

                  else :
                      print("currently we dont have this book")
                      return ""





            
               

            

       



    def return_request(self,user):
        user.history[-1].returN_time = datetime.today()
        self.total_books+=1
        self.cout_taker_of_any_book[ user.history[-1].book_name]+=1
        print("book brrow process done >>")
        print(user.history[-1])




        



######  function for user management 
    def resgister(self,email,password,user):
         self.users[self.next_user_id] = user
         user.iD = self.next_user_id
         self.next_user_id+=1
         print("successfully registered")
         

       
    




   







############################# 
def current_file_testing():
    libray1 = Library('rokamary')
    book1 = Book('tintin', "comic")
    libray1.add_book(book1, 5)
  #  print( libray1.cout_taker_of_any_book)
    book1 = Book('tintin', "comic")
    libray1.add_book(book1, 5)
    book2 = Book('one-piece', "comic")
    libray1.add_book(book2, 5)

    libray1.see_book()
    libray1.remove_book('tintin', "comic")
    libray1.see_book() 
   


if __name__ == "__main__":
    current_file_testing()
