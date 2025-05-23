import time
from order_service import Order
class Restaurant:
    def __init__(self,name,location,timings,ownerDetails,cusine,menu,priceList):
        self.__name=name
        self.location=location
        self.timings=timings
        self.ownerDetails=ownerDetails
        self.cusine=cusine
        self.menu=menu
        self.order=Order(self.menu,priceList)
    @property
    def name(self):
        return self.__name
        
    def registerRestaurant(self):
        print(f"{self.name} is registered")
        self.ownerDetails.displayDetails()
    def open(self):
        print(f"{self.name} is open now. Please order")
    def close(self):
        print(f"{self.name} is closed . Visit Again Tomorrow")
