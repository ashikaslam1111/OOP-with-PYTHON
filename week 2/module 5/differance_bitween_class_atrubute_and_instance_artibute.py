class shop:
    cart =[]
    def __init__(self,byer) :
      self.byer =byer
    def addToCart(self,item):
      self.cart.append(item)


person1 = shop('aslam')
person1.addToCart('phone')
person1.addToCart('sunglass')
print(person1.cart)


person2 = shop('golam')
person1.addToCart('t-shart')
person1.addToCart('iphon')
print(person2.cart) ## so here will be problem cz in cart there will be person1 + person2 item but i should see only person2
## becouse the cart is a calss atribute and so all the people can use it so will be like public tiolet so alls poti will be here 
# if one people use it the tiolet will not be clera instancly 






      