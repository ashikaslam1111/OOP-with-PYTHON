class Order:
    def __init__(self,customer,items) -> None:
        self.customer = customer
        self.total = 0
        self.items = items
        for i in items:self.total+=i.price
        