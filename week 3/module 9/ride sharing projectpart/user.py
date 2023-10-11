from abc import ABC, abstractmethod 
from datetime import datetime 
from collections import deque

class Ride_sharing_company:
    def __init__(self,name) -> None:
        self.name = name
        self.drivers = []
        self.riders = []
        self.ride = []
    
    def add_rider(self,rider):self.riders.append(rider)
    def add_driver(self,driver):self.drivers.append(driver)
    def __repr__(self) -> str:
         return f"Name = {self.name}  total drivers = {len(self.drivers)} and total rider  = {len(self.riders)}"
    

class User(ABC):
    def __init__(self,name,email,nId) -> None:
        self.name = name
        self.email = email
        self.nid = nId
        self.wallet = 0
    @abstractmethod
    def see_user_infl(self):raise NotImplementedError



class Rider(User):
    def __init__(self, name, email, nId,current_location,inital_ballence) -> None:
        super().__init__(name, email, nId)
        self.current_location = current_location
        if inital_ballence>0:self.wallet+=inital_ballence
        self.current_ride = None
        self.my_rides = deque()

    def see_user_infl(self):return f"type rider name = {self.name} ind = {self.nid}"


    def requenst_for_ride(self,my_destination,company):
        requested_ride = Ride_Rwquest(self.current_location,my_destination)
        ride_match =Ride_matcher(requested_ride,company)
        the_driver = ride_match.get_driver()
        if the_driver == None:
            print('all our driver are currently busy please w8')
            return
        
        prepared_ride = Ride(the_driver,self,self.current_location,my_destination)
        print(prepared_ride)
        








class Driver(User):
    def __init__(self, name, email, nId) -> None:
        super().__init__(name, email, nId)
        self.my_rides = deque()

    def see_user_infl(self):return f"type driver name = {self.name} ind = {self.nid}"
     





class Ride:
    def __init__(self,driver,ridder,frm,to) -> None:
       self.driver = driver
       self.rider = ridder
       self.forM = frm
       self.to = to

    def __repr__(self) -> str:
        return f" ridder = {self.rider.name} driver = {self.driver.name} from = {self.forM} to {self.to}"


class Ride_Rwquest:
   def __init__(self,froM,to) -> None:
      self.current = froM
      self.end = to


class Ride_matcher:
    def __init__(self,requested_work,company) -> None:
        # TODO find the best driver fhe rider more advancly
        self.available_drivers = company.drivers
    def get_driver(self):
         if len(self.available_drivers)>0:return self.available_drivers[0]
         return None











#inter action testing
easy_go = Ride_sharing_company('easy_go')
rider1 = Rider('Monir',"hello@abc.com",12345,'nirala',700)
print(rider1.wallet)
driver1  =  Driver('Pappu',"pq@hello.com",223345)
easy_go.add_driver(driver1)
easy_go.add_rider(rider1)
print(easy_go)
rider1.requenst_for_ride('tpi',easy_go)
