from library import*
from book import*
from user import*




def main():
    libray1 = Library('rokamary')
    book1 = Book('tintin', "comic")
    libray1.add_book(book1, 5)
    #libray1.see_book()

    book1 = Book('tintin', "comic")
    libray1.add_book(book1, 5)
    book2 = Book('one-piece', "comic")
    libray1.add_book(book2, 5)
    libray1.see_book()
    #libray1.remove_book('tintin', "comic")
   # libray1.see_book() 
    person1 =  User("aslam")
    person1.register(libray1)
    person1.borrow_book(libray1)
    person1.see_history()



   







if __name__ == "__main__":
    main()