from typing import Any


class family:
    def __init__(self,adrress) -> None:
        self.Adrress = adrress

class school:
    def __init__(self,Class,roll) -> None:
        self.CLass = Class
        self.Roll = roll

class sport:
    def __init__(self,fg) -> None:
        self.favoutite_game = fg


class person(family,school,sport):
    def __init__(self, adrress,Clas,roll,game) -> None:
        family().__init__(self,adrress)
        sport().__init__(self,game)
        school().__init__(Clas,roll)
        
        
        