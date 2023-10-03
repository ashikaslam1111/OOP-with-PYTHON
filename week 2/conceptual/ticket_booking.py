# bus ticket booking system

# Admin
# 1) check available buses
# 2)add a new bus 
# 3)can check bus info


# user 
# 1) check available buses
# 2)can check bus info
# 3)can reserve  seat

class User:
    def __init__(self,userName,password):
        self.name = userName
        self.pasS= password

class buS:
    def __init__(self,coach,driver,arrival,departure,from_des,to):
        self.coach= coach
        self.driver = driver
        self.departure = departure
        self.arrival = arrival
        self.from_des = from_des
        self.to=to
        self.seats = ["empty" for i in range(20)] # it means 20 indexs will be filup with "empty"

class phitron: # it is class for bus company here 
   ## def __init__(self):
    total_bus = 0
    total_bus_list= [] # 
    def add_bus(self):
        bus_no = int(input("enter busNO:"))
        flag =1
        for w in self.total_bus_list:
            if bus_no == w["coach"]:
                print("bus already added")
                flag=0
                break
        if flag:
            bus_driver = input('enter bus driver name>>')
            bus_arrival = input('enter bus arrival time>>')
            bus_departure = input('enter bus departure time>>')
            bus_stform = input('enter bus strat from>>')
            bus_desti = input('enter bus destination>>')
            newbus = buS(bus_no,bus_driver,bus_arrival, bus_departure,bus_stform, bus_desti)
            self.total_bus_list.append(vars(newbus)) # here i use vars functon to keep the bus oject as dictionary
            print("\nbus added succesfully")
            self.total_bus=len(self.total_bus_list)
                   
class counteR(phitron): # as a coutner is belong to a bus company so the counter class inheeite the "phitron"  class
     def reservation(self):
         busNO = int(input("enter the bus no u wanna journy by>>"))
         flag =1
         for w in self.total_bus_list:
             if w["coach"]==busNO:
                 flag=0
                 passenger = input("enter your name>")
                 seat_no = int(input("enter the seat no you want to reserve>"))
                 if seat_no<1 or seat_no>20:print("our seat serial is 1 to 20")
                 else:
                     if w["seats"][seat_no-1]!="empty":
                         print("this seat is already booked")
                     else:w["seats"][seat_no-1]=passenger
             if flag==0:break
         if flag:print(f'no bus found with this no:{busNO}')
         else: print("thanks for taking our service")
        
# main>>>>>2

#bus1 = buS(2,"monir",'12:00pm','12:30pm',"dhake","tangail")

# print(vars(bus1)) # this function give me a key value pair for all the element of the class object

company = phitron()
company.add_bus()
print(vars(phitron))
per1 = counteR()
per1.reservation()
per1.reservation()