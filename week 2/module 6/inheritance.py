
class Gadget: # it is base class
    def __init__(self,brand,price,color) -> None:
        self.Brand = brand
        self.Color = color
        self.Price = price

    def run(self):
        return f"running laptop {self.Brand}"



class laptop(Gadget):
    def __init__(self,brand,price,color,mamory) :
        self.Memory=mamory
        super().__init__(brand,price,color)
    def __repr__(self) -> str:
        return f""" 
        LAPTOP BRAND IS {self.Brand}
        PRICE IS {self.Price}
        COLOR IS {self.Color}
        MAMORY IS {self.Memory} gb
        """
    
    
    

class phone:
    def __init__(self,duel_sim):
        self.sim2= duel_sim
    def phon_call(self,number,text):
        return f"sending sms to {number} with {text}"
    

class camare:
    def __init__(self,pixel) -> None:
        self.Pixel = pixel











# main.............

my_pc = laptop('acer',35000,"black",500)



print(my_pc)




