class Account:
    def __init__(self,name,number):
            self.name=name
            self.number=number
            self.transuction=10
            self.loon_bound=200
    def deposit(self,amount,balance):
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