class BankAccount():

    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"{self.balance} is your total credits after Deposition of {amount} credits\n")

    def withdraw(self,amount):
        if amount>(self.balance):
            print('less funds available in your account to make this transaction\n')
        else:
            self.balance=self.balance-amount
            print(f"{amount} has been withdrwan from your account\nYour account balance is now {self.balance}")
    def __str__(self):
        return f"{self.owner} has {self.balance} in his account\n"

name=input("enter account holder name\n")
cents=int(input('enter the amount to deposit\n'))
account=BankAccount(name,cents)
print(account)
while True:
    x=int(input("enter the option--\n1.withdraw\n2.deposit\n3.exit\n"))
    if x==1:
        amount=int(input('Enter amount to withdraw\n'))
        account.withdraw(amount)
    elif x==2:
        depo=int(input('Enter amount to deposit\n'))
        account.deposit(depo)
    else:
        quit("thanks for using ")