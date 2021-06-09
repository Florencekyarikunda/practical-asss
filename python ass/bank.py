from datetime import date, datetime, time
class Account:
    def __init__(self,name,number):
            self.name=name
            self.number=number
            self.transuction=10
            self.loon_bound=200
            self.transuction=[]
    def deposit(self,amount,balance):
        transuction={
            "amount":amount,
            "balance":self.balance,
            "naration":"You deposited",
            "time":datetime.now()
        }
        self.statement.append(transuction)
        return f"Hello you have repaid your loan  and your balance is UGsh{self.deposit}"
        self.amount=amount
        self.balance=balance


        if amount<=0:
            return "deposit a valid amount"

        else:  
            self.balance += amount
        
        return f"Hello {self.name}, You have deposited {amount},your new balance is {self.balance}."
         
    def withdraw(self,amount):
        totalwithdraw=amount+self.transaction

        if amount<=0:
                return "the valid amount"
        elif totalwithdraw>self.balance:
            return "insufficient balance"

        else: 
            self.balance==totalwithdraw
            return "Hello {self.name},you have successfull transuctions and your balance is {self.balance}."

    def borrow(self,amount_loan):
        total=self.interest*amount_loan
        amount_loan=amount_loan+total
        if amount_loan>self.loon_bound:
            return f"Hello you have borrowed {self.loan} and your balance is {amount_loan-self.loan}."
        elif amount_loan<self.loon_bound:
            return "your loan amount is too much"
        elif amount_loan>0:
            return "you cannot borrow"
        else:
            self.loon_bound=total
            self.balance+=amount_loan
        return (f"Hello you have repayed {self.loan} and your balance is {amount_loan+self.loan}.")

def statement(self):
    for transuction in self.transuction:
        amount=transuction["amount"]
        narration=transuction["narration"]
        balance=transuction["balance"]
        time=transuction["time"]
        date=transuction["date"]
    print (f"{amount}....{date}.... {narration}.... {amount}....balance {balance}.")

def repay(self,amount):
        if amount <0:
            return f"Enter a valid amount"
        elif amount<=self.loan:
            self.loan-=amount
            return f"you have repaid  your loan and your balance is UGsh{self.loan}"
        else:
            differ=amount-self.loan
            self.loan=0
            