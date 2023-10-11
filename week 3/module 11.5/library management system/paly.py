

class User:
    def __init__(self,name,email,password) -> None:
        self.name = name
        self.email=email
        self.password=password


class Server:
    def __init__(self) -> None:
      self.users = []
        
    def login(self,email,password):
        for user in self.users:
            if user.email == email:
                if user.password == password:
                    print("successfully login")
                else : print("password is wrong")
                return None
        print("no user found with this email")

    def resgister(self,name,email,password):
       new_user =  User(name,email,password)
       self.users.append(new_user)





# testing zone

sever1 =Server()

while True:
   print("\n1. Register")
   print("2. Login")
   print("3. Exit")

   flag = int(input("enter your choice>>"))
   if flag==1:
      name =input("enter your name >>")
      email =input("enter your email >>")
      password=input("enter your password>>")

      sever1.resgister(name,email,password)

   elif flag == 2:
       email =input("enter your email >>")
       password=input("enter your password>>")
       sever1.login(email,password)
   else :
       print("have good day see you again")
       break


