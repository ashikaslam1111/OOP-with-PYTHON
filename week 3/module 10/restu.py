
class Restrurent:
    def __init__(self,name,rent,mane = []) -> None:
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.menu = mane
        self.revenue=0
        self.profit = 0
        self.expence = 0
        self.balence =0
        self.rent = rent
        self.orders=[]

    
    def add_employ(self,employ_type,employ):
        if employ_type == "chef":
           self.chef=  employ
        elif employ_type == "server":
             self.server=employ
        elif employ_type == "manager":
            self.manager=employ

    def recive_payment(self,amount,customer,order):
        self.revenue+=order.total
        customer.due_amount=0
        self.balence+=order.total
        return amount - order.total
    
    def pay_ecpance(self,amount,description):
        if amount<=self.balence:
            self.expence+=amount
            self.balence-=amount

            print("ecpance for",description," tk ",amount)
        else: print("sorry not enough mouny ")
    
    def pay_salary(self,employ):
        if employ.salary<=self.balence:
           employ.recive_salary()
        else:print("sorry not enough money")

    def show_employ(self):
        print(f"manger =  {self.manager.name} server = {self.server.name}  chef  = {self.chef.name}")
    

    def add_orders(self,order):self.orders.append(order)




