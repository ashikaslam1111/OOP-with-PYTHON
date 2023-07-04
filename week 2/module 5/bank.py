
class bank:
    def __init__(self,balence) :
        self.balence= balence
        self.min_withdrae=100
        self.max_withdrae=100000

    def get_balenc(self):
        return self.balence
    
    def deposit(self,amount):
        if amount>0:
            self.balence+=amount

    def withdraw(self,amount):
        if amount <self.min_withdrae:
            return f'you can not witdraw less then {self.min_withdrae}'
        elif(amount>self.max_withdrae):
             return f'you can not witdraw more then {self.max_withdrae}'
        elif(amount>self.balence):
             return f'your current ballance is only {self.balence}'
        else:
            self.balence-=amount
            return f"""
                    withdraw successfull!! 
                    yor width draw ammoutn is {amount}
                    your current balence is {self.balence}
                    """
person1 = bank(1000)
print(person1.withdraw(100))




