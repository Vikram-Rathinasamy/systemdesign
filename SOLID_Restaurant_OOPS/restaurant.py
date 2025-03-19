from abc import *
import time
class Resto(ABC):
    @abstractmethod
    def open(self):
        pass
    def close(self):
        pass
class Location:
    def __init__(self,city,state,pincode):
        self.city=city
        self.state=state
        self.pincode=pincode
class Menu():
    def __init__(self,food_items={}):
        self.foods=food_items
    def addMenu(self,food):
        self.foods.add(food)
    def deleteMenu(self,food):
        self.foods.remove(food)
    def getFoodPrice(self,food):
        return self.foods.get(food,0)
#Liskov substituion princinple
class Dessert(Menu):
    def __init__(self,timings,food_items={}):
        super().__init__(food_items)
        self.timings=timings
    def isOpen(self):
        #time check
        print("Yes, We take orders on Desserts")
        
class Kitchen():
    @staticmethod
    def prepareFood(food_item):
        print(f"Food {food_item} is being prepared")
        time.sleep(5)
        print(f"{food_item} is prepared, Ready to serve")
        return 1
#Interface segregation principle
class OrderFood(ABC):
    @abstractmethod
    def takeOrder(self,food_item,tableNo,userLocation):
        pass
class DineIn(ABC):
    @abstractmethod
    def serveFood(self,food_item,tableNo):
        pass
    
class Delivery(ABC):
    @abstractmethod
    def deliverFood(self,food_item,userLocation):
        pass

class DineinSevervice(OrderFood,DineIn):
    def __init__(self,menu):
        self.menu=menu
    def takeOrder(self,food_item,tableNo=0,userLocation=None):
        if food_item not in self.menu.foods:
            print(" oh oh Sorry! Item not available.")
            return
        if Kitchen().prepareFood(food_item):
            return self.serveFood(food_item,tableNo)
    def serveFood(self,food_item,tableNo):
        print(f"Serving Hot {food_item} to table {tableNo}")
        
class DeliverySevervice(OrderFood,Delivery):
    def __init__(self,menu):
        self.kitchen=Kitchen()
        self.menu=menu
    def takeOrder(self,food_item,tableNo=0,userLocation=None):
        if food_item not in self.menu.foods:
            print(" Sorry Item not served")
            return
        if self.kitchen.prepareFood(food_item):
            return self.deliverFood(food_item,userLocation)
    def deliverFood(self,food_item,userLocation):
        print(f"Delivering {food_item} to {userLocation}")

#Interface seggregation 
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
class CardPayment(ABC):
    @abstractmethod
    def swipe(self,amount):
        pass

class CashPayment(Payment):
    def pay(self,amount):
        print (f"{amount} Paid in cash")
        return 1
        
class CreditCardPayment(Payment,CardPayment):
    def pay(self,amount):
        if self.swipe(amount):
            print (f"{amount} Paid in credit card")
            return 1
        return 0
    def swipe(self, amount):
        return 1
class DebitCardPayment(Payment,CardPayment):
    def pay(self,amount):
        if self.swipe(amount):
            print (f"{amount} Paid in Debit card")
            return 1
        return 0
    def swipe(self, amount):
        return 1

class PaymentService:
    #Dependecy Invertion, Open closed Principle
    def processPayment(self,amount,payment_method:Payment):
        if (payment_method.pay(amount)):
            return "Paid successfully"
        return "Error in Payment"
#Single Responsiblity principle
class Restaurant(Resto):
    all_restaurants=[]
    def __init__(self,name,cusine,timing,location,owner,orderService,paymentService):
        #Asserts 
        assert owner!=None,("Owner cannot be None")
        #Assignemts
        self.__name=name
        self.cusine=cusine
        self.timing=timing
        self.location=location
        self.__owner=owner
        self.orderservice=orderService
        self.paymentService=paymentService
        self.totalBill=0
        
        Restaurant.all_restaurants.append(self)
        
    @property 
    def name(self):
        return self.__name
    @name.setter
    def name(self,val):
        if len(val)<5:
            raise Exception("Name is too short")
        self.__name=val
    @property
    def owner(self):
        return self.__owner
    
    #Open closed principle
    def take_order(self,food_item,tableNo=0,userLocation=None):
        self.orderservice.takeOrder(food_item,tableNo,userLocation)
        self.totalBill+=self.orderservice.menu.getFoodPrice(food_item)
        
    def open(self):
        print (f"Restaurant {self.name} owned by {self.owner} is now open. Serving {self.cusine} foods at High Quality...")
    def close(self):
        print (f"Restaurant {self.name} is closed , will open tomorrow @ {self.timing}")
        
    def payment(self,payment_method):
        print("Total bill to Pay",self.totalBill)
        print(self.paymentService.processPayment(self.totalBill,payment_method))
        
