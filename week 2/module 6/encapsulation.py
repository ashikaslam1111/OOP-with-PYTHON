# access modifiar i) public  ii)protected  iii) private


class bank:
    def __init__(self,deposit) -> None:
        self.__balence=0 # here i use "__" it before balence to make privat so the the user cna not change the value
        self.__balence+=deposit


# " " normal public,"_" wanna treat as protecdted, "__" it is private
    def chek_mony(self):return self.__balence




# main ..................

person1 = bank(100)

 ## person1.__balence=900  this line wont work

# print(person1.chek_mony())



## the way we can access private variable

print(dir(person1))

print(person1._bank__balence)
