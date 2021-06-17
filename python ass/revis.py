class BankAccount:
    def __init__(self,name,natinality):
        self.name=name
        self.nationality=natinality
        self.balance=0
      
    def deposit(self):
        amount=float(input("Enter the amount to be deposited:" ))
        self.balance+=0
        print("\n Amount deposited:", amount)


    def withdraw(self):
        amount=float(input("Enter amount to be withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You withdrew: ", amount)
        else:
            print("\n Insufficient balance ")

    def remain(self):
        print("\n Net Available Balance=", self.balance)


        