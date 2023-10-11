from datetime import datetime

class Recieve:
    def __init__(self,user,book) -> None:
        self.name = user.name
        self.book_name = book.name 
        self.catagory =book.catagory
        self.borrow_time = datetime.today()
        self.returN_time  = None

    def __repr__(self) -> str:
        return f"""
 ---------- YOUR RECIEVE ----------       
        { self.name}
        { self.book_name }
        { self.catagory }
        { self.borrow_time }
        { self.returN_time}
        """


        