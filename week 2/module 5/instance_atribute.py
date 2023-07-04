class shop:
    cart =[]# claass atribte and its prioritu is 2nd { if  have smae name with a same data type}
    def __init__(self,byer):
        self.byer=byer
        self.cart=[] # it is a intance atribute cz we made using self
        # i made a arry whic is calss atribute with the same name but by defult the instance atribute wiil be access

    
    def adTocart(self,item):
        self.cart.append(item)


person1 = shop('aslma')
person1.adTocart('watch')
person1.adTocart('cock')
print(person1.cart)

person2 = shop('golam')
person2.adTocart('tshart')
person2.adTocart('phon')
print(person2.cart)
