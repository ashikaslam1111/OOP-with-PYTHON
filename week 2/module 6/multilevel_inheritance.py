class vehicle:
    def __init__(self,name,price) -> None:
        self.Name = name
        self.Price =price
    def move(self):
        pass
    def __repr__(self) -> str:
        return f"""
        Name is {self.Name}
        Price is {self.Price}
        """

class bus(vehicle):
    def __init__(self, name, price,sit) -> None:
        self.Sit = sit
        super().__init__(name, price)
    def __repr__(self) -> str:
        return super().__repr__()
        
        

class track(vehicle):
    def __init__(self, name, price,weight) -> None:
        self.Weight = weight
        super().__init__(name, price)

class pick_up(track):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)



class acbus(bus):
    def __init__(self, name, price, sit,temprature) -> None:
        self.cool = temprature
        super().__init__(name, price, sit)
    def __init_subclass__(cls) -> None:
        return f" it is a bus "
        
    


# main................

my_green_buss = acbus("clasic",500000,25,16)
print(my_green_buss)

        