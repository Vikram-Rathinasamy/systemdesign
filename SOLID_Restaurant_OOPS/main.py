from restaurant import *
print("Welcome")
rest1Location=Location("Bangalore","Karnataka",560077)
food_items={"Idly":50,"Mysore Masala Dosa":100,"Ghee Ven Pongal":99,"Vada":30}
dineIn=DeliverySevervice(Menu(food_items))
paymentService=PaymentService()
rest1=Restaurant("Mysore Cafe","South Indian","7.00 Am to 1.00 Am",rest1Location,"Saj",dineIn,paymentService)
rest1.open()
userInput=input("Please order the Items: ")
rest1.take_order(userInput,0,"Hive coliving")
userInput=input("Please order the Items: ")
rest1.take_order(userInput,0,"Hive coliving")
userInput=input("Ready to Pay, say Yes ")
if userInput=="Yes":
    userInput=input("Say yes to pay via Debit card:")
    rest1.payment(DebitCardPayment())
    print("Thanks for visiting")
    rest1.close()
