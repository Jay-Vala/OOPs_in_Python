# Create an Account Class and get its Balance, Debit money from account and credit money to the account
class Account():
    
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def getBalance(self):
        return self.balance
    
    def debit(self, amount):
        if self.balance > amount:
            self.balance -= amount
            # return self.balance
            print(f"Balance Debited: Rs. {amount}")
            print(f"Total Balance: {self.getBalance()}")
        else:
            print("Insufficiant Balance")
    
    def credit(self, amount):
        self.balance += amount
        print(f"Balance Credited: Rs. {amount}")
        print(f"Total Balance: {self.getBalance()}")
    

ac1 = Account(5876123,1000)

ac1.debit(5000)
ac1.credit(500)