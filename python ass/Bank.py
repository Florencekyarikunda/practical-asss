class Bank:
    def __init__(self):
      
        self.balance=0
        print("The account is created") 

    def deposit(self):
            amount=float(input("Enter the amount deposited: "))
            self.amount=self.balance + amount
            print("Deposit is successfully and the balance in the account is % f" % self.balance)
    def withdraw(self):
        amount=float(input("Enter the amount to withdraw: "))
        if(self.balance>=amount):
            self.balance=self.balance-amount
            print("The withdraw is successfull and the balance is %" % self.balance")
        else:
            print("Insufficient balance")

    def enquiry(self):
            print("Balance in the account is %" %self.balance)
   
   






    