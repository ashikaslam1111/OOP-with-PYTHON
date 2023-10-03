

class animal:
    def __init__(self,name) -> None:
         self.Name = name
    def make_sound(self):
         print(f"{self.Name} is making sund")


class cat(animal):
     def __init__(self, name) -> None:
          super().__init__(name)
     def make_sound(self):
         print(f"mew mew im {self.Name}  mew")


class dog(animal):
     def __init__(self, name) -> None:
          super().__init__(name)
     def make_sound(self):
         print(f"gew gew im {self.Name}  gew")

        



class unknown_amimal(animal):
     def __init__(self, name) -> None:
          super().__init__(name)





# main................

cat1 = cat('pussy')
cat1.make_sound()


dog1=dog('deshiKutta_boltu')
dog1.make_sound()


unknown_amimal1=unknown_amimal("mr_x")
unknown_amimal1.make_sound()