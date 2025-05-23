from restaurant import *
from order_service import DineIn,TakeAway
from payment_service import *
from data import *
#Main class handler
class Location:
    def __init__(self,place,googleMap,zipcode):
        self.place=place
        self.googleMapLoaction=googleMap
        self.zipcode=zipcode
    def displayDetails(self):
        print(self.place, self.zipcode)
location=Location("WhiteField","Pinned location","560037")
class Owner:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def displayDetails(self):
        print("Displaying owner details...")
        print(self.name, self.age)
owner=Owner("Saju & Subbu",28,"Female and Male")
print("New Restaturant in registration process...")
restaurantObj=Restaurant("Mysore Cafe",location,"5.00 am - 11 pm",owner,"South Indian",menuData,priceData)
print("Name : ",restaurantObj.name)
restaurantObj.registerRestaurant()
print(f"Welcome to {restaurantObj.name}")
restaurantObj.open()
userInput=int(input("Press 1 for dine in or 2 for Delivery serice: "))
serveObj=None
if userInput==1:
    tableNo=int(input("Enter table no to dine in: "))
    serveObj=DineIn(tableNo)
else:
    address=input("Enter the location to deliver:")
    serveObj=TakeAway(address)

def getPaymentObj():
    restaurantObj.order.displayBill()
    paymentType=str(input("Please enter the payment type: "))
    if paymentType=="credit card":
        paymentObj=CreditCard("visa")
    elif paymentType=="debit card":
        paymentObj=DebitCard("rupay")
    elif paymentType=="UPI":
        print("Please scan the QR code...")
        paymentObj=UPI()
    else:
        amount=int(input("Please enter amount to give in Rs."))
        paymentObj=CashPayment(amount)
    return paymentObj
while True:
    time.sleep(2)
    userData=int(input("Would like to order, Press 1 for yes 0 otherwise: "))
    if userData:
        food_item=str(input("Ready to take the order. Please say what you want to have.."))
        restaurantObj.order.takeOrder(food_item,serveObj)
    else:
        paymentObj=getPaymentObj()
        restaurantObj.order.pay_bill(paymentObj)
        serveObj.clearOrder(Order.all_orders)
        break
print("Thank you visit Again..")
print("Total orders: ",Order.all_orders)