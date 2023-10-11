class Food:
    def __init__(self,name,price) -> None:
        self.name  = name
        self.price = price
        self.cook_time = 15


class Burger(Food):
    def __init__(self, name, price,meat,ingredients) -> None:
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients
    def __repr__(self) -> str:
        return f"name = {self.name}  price = { self.price}"


class Pizza(Food):
    def __init__(self, name, price,size,ingredients,toppings) -> None:
        super().__init__(name, price)
        self.size = size
        self.ingredients = ingredients
        self.topings = toppings

    def __repr__(self) -> str:
        return f"name = {self.name}  price = { self.price}"


class Drinks(Food):
    def __init__(self, name, price,is_cold = True,) -> None:
        super().__init__(name, price)
        self.iScold = is_cold
    def __repr__(self) -> str:
        return f"name = {self.name}  price = { self.price}"



class Menu:
    def __init__(self) -> None:
        self.pizzas =[]
        self.burgers =[]
        self.drinks = []

    def add_manu_item(self,item_type,item):
        if item_type == 'pizza':self.pizzas.append(item)
        elif item_type == 'burger':self.burgers.append(item)
        elif item_type == 'drink':self.drinks.append(item)


    def kick_pizza(self,pizza):
        self.pizzas.remove(pizza)


    def show_menu(self):
        for i in self.pizzas:
            print(f"name = {i.name} price {i.price}")

        for i in self.burgers:
            print(f"name = {i.name} price {i.price}")

        for i in self.drinks:
            print(f"name = {i.name} price {i.price}")


        
