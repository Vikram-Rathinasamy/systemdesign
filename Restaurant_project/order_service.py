import time
from abc import *
#Interface seggregation princinple
class OrderService(ABC):
    @abstractmethod
    def serveOrder(food_item):
        pass
class OnlineDeliveryService(OrderService):
    @abstractmethod
    def deliverFood():
        pass
class DineinSerive(OrderService):
    @abstractmethod
    def serveFoodToTable():
        pass

class Order:
    all_orders=[]
    def __init__(self,menuItems,priceList):
        self.menuItems=menuItems
        self.priceList=priceList
        self.kitchen=Kitchen()
        self.totalBill=0
        
    def takeOrder(self,food_item,foodServiceObj:OrderService):
        if food_item in self.menuItems:
            if(self.kitchen.prepareFood(food_item)):
                #Dependency inversion principle by calling it with interface
                foodServiceObj.serveOrder(food_item)
                time.sleep(5)
            self.menuItems[food_item]-=1
            if self.menuItems.get(food_item,0)<=0:
                self.menuItems.pop(food_item)
            self.totalBill+=self.priceList.get(food_item,0)
            Order.all_orders.append(food_item)
        else:
            print("Sorry the food is not available! Please order something else")

    def pay_bill(self,paymentObj):
        
        if(paymentObj.pay(self.totalBill)):
            print("Payment Successful :)")
        else:
            print("Payment failed :( , Please try diff method")
    def displayBill(self):
        print("Total Bill to pay :",self.totalBill)


class Kitchen:
    def prepareFood(self,foodItem):
        print("Preparing food:",foodItem)
        time.sleep(5)
        return True


class DineIn(DineinSerive):
    def __init__(self,tableNo):
        self.tableNo=tableNo
        print(f"Table {tableNo} is sanitized and ready for Dinein")
    def serveOrder(self,food_item):
        print(f"Food {food_item} is ready for Dine in ")
        self.serveFoodToTable(food_item)
        print("Food is serviced.")

    def clearOrder(self,totalItems):
        print("Table served items: ",totalItems)
        print("Table is sanitized after customer paid the bill.")
    def serveFoodToTable(self,food_item):
        time.sleep(5)
        print(f"{food_item} is served to table {self.tableNo}")

class TakeAway(OrderService):
    def __init__(self,address):
        self.address=address
        print(f"Delivery address noted: {address}")
        
    def serveOrder(self,food_item):
        print(f"Food {food_item} is ready for Delivery ")
    def clearOrder(self,items):
        self.deliverFood(items)

    def deliverFood(self,items):
        time.sleep(5)
        print(f"{items} is Delivered to address {self.address}")
    


        
    

