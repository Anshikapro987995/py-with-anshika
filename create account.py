class Account():
    def __init__(self,balance,account):
        self.balance=balance
        self.account=account
    def debit(self,amount):
       self.balance-=amount 
       print("rs",amount,"was debited") 
       print("total balance is",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("rs",amount,"was credited")
        print("total balance is",self.get_balance())
    def get_balance(self):
        return self.balance         
acc1=Account(20000,123)
print(acc1.balance,acc1.account) 
acc1.debit(6000) 
acc1.credit(12000)
print(acc1.get_balance()) 
print("thanks")    