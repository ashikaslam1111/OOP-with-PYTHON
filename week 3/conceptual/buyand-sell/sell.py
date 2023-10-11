import datetime
class Sell:
    def __init__(self,product,customer,seller) -> None:
        self.por = product
        self.seller = seller
        self.custo = customer
        self. time = datetime.datetime.now()

    def __repr__(self) -> str:
        return f"""
        PRODUCT NAME IS  ={self.por.name}
        PIRCE IS  ={ self.por.price}
        CUSTOMER IS ={self.custo.name}
        SELLER IS { self.seller.name}
        TIME IS = {self.time}
        """
        