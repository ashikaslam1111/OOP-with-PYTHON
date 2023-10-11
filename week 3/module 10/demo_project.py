from abc import ABC,abstractmethod
class User(ABC):
    def __init__(self,name,phone,email,addess) -> None:
        self.name =name
        self.phone = phone
        self.email=email
        self.address = addess

class Customer(User):
    def __init__(self, name,phone,email,addess,money) -> None:
        super().__init__(name,phone,email,addess)
        self.wallet = money
        self.__order = None
        self.bill = 0
        self.due_amount =self.bill
    
    # @property
    # def order(self):return self.__order
    # @order.setter
    # def set_order(self,order):self.__order=order

    def place_order(self,order):
        self.order = order
        self.bill+=order.total
        print(f"{self.name} palced an order item are {order.items}")
    
    def eat(self):
        print(f"{self.name} is eating {self.order.item}")


    def pay_for_order(self,amoung):
        pass

    def give_tips(self,tips_amount):
        pass

    def write_reiviwe(self,tars):
        pass

    

class Employe(User):
    def __init__(self, name, phone, email, addess,salary,department,starting_date,nid) -> None:
        super().__init__(name, phone, email, addess)
        self.salary = salary
        self.department = department
        self.satrting_date = starting_date
        self.nid = nid
        self.due = salary

    def recive_salary(self):
        self.due = 0



    
class Chef(Employe):
    def __init__(self, name, phone, email, addess, salary, department, starting_date, nid,cooking_item) -> None:
        super().__init__(name, phone, email, addess, salary, department, starting_date, nid)
        self.cook_item = cooking_item

class Server(Employe):
    def __init__(self, name, phone, email, addess, salary, department, starting_date, nid) -> None:
        super().__init__(name, phone, email, addess, salary, department, starting_date, nid)

        self.tips_earning = 0

    def take_order(self,order):
        pass

    def transfer_oder_to_chef(self,order):
        pass

    def serve_the_food(self,order):
        pass

    def recive_tips(self,amount):
        self.tips_earning+=amount






class Manager(Employe):
    def __init__(self, name, phone, email, addess, salary, department, starting_date, nid) -> None:
        super().__init__(name, phone, email, addess, salary, department, starting_date, nid)



















