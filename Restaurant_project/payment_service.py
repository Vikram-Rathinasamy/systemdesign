from abc import *
import time
#Open closed principle + Interface seggregation+Liskov substitution principle.
class PaymentType(ABC):
    @abstractmethod
    def pay():
        pass

class CashPaymentMethod(PaymentType):
    @staticmethod
    def returnChange():
        pass

class CreditCard(PaymentType):
    acceptedCards=set(["visa","mastercard"])
    def __init__(self,cardType):
        self.cardType=cardType
    def pay(self,amount):
        if self.cardType not in CreditCard.acceptedCards:
            print(f"{self.cardType} card is not accepted here, Please try differnt card/payment method ")
            return False
        print(f"Credit card payment processing:{amount}.....")
        time.sleep(5)
        return True
    
class DebitCard(PaymentType):
    acceptedCards=set(["visa","rupay"])
    def __init__(self,cardType):
        self.cardType=cardType
    def pay(self,amount):
        if self.cardType not in DebitCard.acceptedCards:
            print(f"{self.cardType} card is not accepted here, Please try differnt card/payment method ")
            return False
        print(f"Debit card payment processing :{amount}.....")
        time.sleep(5)
        return True
    
class UPI(PaymentType):
    def pay(self,amount):
        print(f"UPI payment processing :{amount}.....")
        time.sleep(5)
        return True
    
class CashPayment(CashPaymentMethod):
    def __init__(self,amountGiven):
        self.amountGiven=amountGiven
    @staticmethod
    def calculateReturn(a,b):
        return a-b
    def pay(self,amount):
        if self.amountGiven<amount:
            print(f"{self.amountGiven-amount} extra needed. ")
            return False
        print(f"{amount} paid in Cash . Remaining to return {self.amountGiven-amount}")
        time.sleep(2)
        print(f"Remaining {CashPayment.calculateReturn(self.amountGiven,amount)} Change is returned.")
        time.sleep(2)
        return True
    
