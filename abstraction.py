from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def bank_revenue(self):
        pass

class OwnerBalance(BankAccount):
    def bank_revenue(self):
        return "Owner has a lot of money"

    def __str__(self): 
        return "OwnerBalance Object"

taka = OwnerBalance()
               
print(taka.bank_revenue()) 
