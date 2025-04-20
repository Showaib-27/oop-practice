class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       
        self._bank_name = "ABC Bank"  
        self.__balance = balance 

    def get_balance(self):  
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

account = BankAccount("Alice", 1000)
print(account.owner)       # ✅ Public, accessible
print(account._bank_name)  # ✅ Protected, accessible but discouraged
print(account.get_balance()) # ✅ Accessing private via method
# print(account.__balance)  # ❌ Error: Private variable

account.deposit(500)
print(account.get_balance()) # ✅ Updated balance: 1500
