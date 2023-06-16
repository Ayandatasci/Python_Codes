class bank_account:
    def __init__(self, balance):
        self.__balance= balance
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        return self.__balance

    def withdraw(self, amount):
        if self.__balance >= amount: 
            self.__balance = self.__balance - amount
            return self.__balance
        else: 
            return "Insufficient Balance"
    
b1= bank_account(7000)
print(b1.deposit(4000))
print(b1.withdraw(43000))