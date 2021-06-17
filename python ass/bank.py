from datetime import  datetime
class Account:
    def __init__(self,name,number):
            self.name=name
            self.number=number
            self.loon=0
            self.balance=0
            self.statement=[]
            
    def show_balance(self):
        return f"your balance is {self.balance}"
    def deposit(self,amount):
        try:
            amount + 10
        except TypeError:
            return f"please enter {amount} in figures"
        if amount<=0:
            return "deposit a valid amount"
        else:  
            self.balance += amount
            # now=datetime.now()
            transuction={
            "amount":amount,
            "balance":self.balance,
            "naration":"You deposited",
            "time":datetime.now()
             }
            self.statement.append(transuction)
            return self.show_balance()
    def get_statement(self):
        for transuction in self.statement:
            amount=transuction["amount"]
            narration=transuction["narration"]
            balance=transuction["balance"]
            time=transuction["time"]
            # date=transuction["date"]
            date= time.strftime("%D")
            print (f"{amount}....{date}.... {narration}.... {amount}....balance {balance}.")
    
    def withdraw(self,amount):
        totalwithdraw=amount+self.transaction
        if amount <= 0:
                return "the valid amount"
        elif totalwithdraw>self.balance:
            return "insufficient balance"

        else: 
            self.balance==totalwithdraw
            return "Hello {self.name},you have successfull transuctions and your balance is {self.balance}."

    def borrow(self,amount):
        try:
           amount * 10
        except TypeError:
            return f"please enter the amount in figures" 
        total=self.interest*amount
        amount=amount +total
        if amount>self.loan:
            return f"Hello you have borrowed {self.loan} and your balance is {amount-self.loan}."
        elif amount<self.loon:
            return "your loan amount is too much"
        elif amount>0:
            return "you cannot borrow"
        else:
            now=datetime.now()
            transuction={
            "amount":amount,
            "balance":self.balance,
            "naration":"You deposited",
            "time":now
             }
            self.loan = total
            self.balance += amount
        return (f"Hello you have repayed {self.loan} and your balance is {amount+self.loan}.")

    # def get_statement(self):
    # for transuction in self.transuction:
    #     amount=transuction["amount"]
    #     narration=transuction["narration"]
    #     balance=transuction["balance"]
    #     time=transuction["time"]
    #     date=transuction["date"]
    # print (f"{amount}....{date}.... {narration}.... {amount}....balance {balance}.")
 
    def repay(self,amount):
        try:
            amount - 10
        except TypeError:
            return f"please enter the amount in figures"
        if amount <0:
            return f"Enter a valid amount"
        elif amount <= self.loan:
            self.loan-=amount
        else:
            differ = amount - self.loan
            self.loan = 0
            return f"you have repaid  your loan and your balance is UGsh{self.loan_bound}"
        
    def transfer(self,amount,account):
        try:
            amount > 0
        except TypeError:
            return f"please enter the amount in figures"
            fees=amount * 0.05
            total=amount + fees
        if amount > self.balance.account:
            return f"Your balance is {self.balance} your {self.total} in order to transfer {self.total}"
        else:
                self.balance-=amount
                account.deposit(amount)
                return f"Yello, you have received {self.amount} and trunsuction fees is{self.fees}"

class mobilemoneyAccount(Account):
    def __init__(self,name,number,serviceprovider):
        Account __init__(self,name, number)
        self.serviceprovider= serviceprovider

    def buyairtime(self,amount):
        try:
            amount+100
        except TypeError:
            return f"please enter the amount in figures"
        
        if amount<=0:
            return f"You cannot buy an airtime of shillings {amount} because your balance is too low"
        
        else:
            self.balance-=amount
            transaction={"amount":amount,"balance":self.balance,"narration":"you have purchased","time":datetime.now()}
            self.transaction.append(transaction)
            return f"Your balance is shs{amount} in your account balance is {self.balance}"




    