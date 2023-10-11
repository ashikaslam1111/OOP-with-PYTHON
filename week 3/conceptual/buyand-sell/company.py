from sell import*

class Company:
    def __init__(self,name) -> None:
       self.name = name
       self.users  =  []
       self.prducts = []
       self.profit = 0
       self.total_deal = 0
       self.count_of_sell =0
       self.users_and_pass={}
       self.productsmap = {}## with we will confirm that we have the product
       self.product_owner ={}
       self.porwith_name = {}
       self.sell =[]

    
    def _show_product(self):
        for i in self.prducts:print(i)

    def make_new_user(self,user):
        
        if user in self.users :print ("you are already a uer of our site")
        else:
            password1  = input("enter your password")
            password2 = input("re-enter your password")
            if password1==password2:
                self.users.append(user)
                print("successfully singed up")
            else:print("passwords are not matchig tyr agint")

    def customer_want_to_buy(self,customer):
        print ("-------see uor all products---------")
        for i in  self.prducts:print(i)
        flag = int(input("for bying somethig press 1>>"))
        if flag==1:
            pro =input("enter the name of the product you wanna buy>>")
            if self.productsmap[pro]>0:
                porx =self.porwith_name[pro]
                malik = self.product_owner[porx]
                pirce = porx.price
                if customer.wallate>= pirce:
                      self.total_deal+= pirce 
                      self.profit+=pirce*(0.05)
                      self.count_of_sell+=1
                      customer.wallate-= pirce
                      malik.wallate+=pirce
                      new_sell = Sell(porx,customer, malik)
                      self.sell.append(new_sell)
                      print("your resip is",new_sell)



                   

                else : print("to continue you need to add money in your wallte so load money and then come agin")


                
            else :print("sorry we do not have it")

        else :print("see again")
        

    def add_product(self,product,user):
      self.prducts.append(product)
      self .productsmap[product.name]=1
      self.product_owner[product]=user
      self.porwith_name[product.name]=product




