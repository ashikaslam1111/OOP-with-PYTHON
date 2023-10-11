
class User:
    def __init__(self,name,nid,email,) -> None:
       self.name =name
       self.nid = nid
       self.email = email
       self.wallate = 0

    def load_money(self,amounot): 
        if amounot>0:self.wallate+=amounot

    def see_product(self,company):company. _show_product()
    
    def buy_product(self,company): company.customer_want_to_buy(self)


    def post_for_sell(self,product,company):
        company.add_product(product,self)

    def _creat_id(self, compny):compny.make_new_user(self)
