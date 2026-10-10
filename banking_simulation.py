class Account:
    def __init__(self,id,holder_name):
        self.id=id
        self.holder_name=holder_name
        self._balance=0 #encapsulation 
    def check_balance(self):
        print(f"Balance: {self._balance}")
    def deposit(self,amount):
        self._balance+=amount
        return self._balance
    def withdraw(self,amount):
        if self._balance>=amount:
            self._balance-=amount
            print(f"withdrawn amount: {amount}")
            print(f"remaining balance: {self._balance}")
        else:
            print("you are not having sufficient balance!!")
class SavingsAccount(Account):#inheritance
    def __init__(self,id,holder_name):    
        super().__init__(id,holder_name)
        self.intrest_rate=5
    def calculate_intrest(self):
        print("####savings account###")
        return self._balance*self.intrest_rate/100
class CurrentAccount(Account): #inheritance
    #overdraft limit
    def __init__(self,id,holder_name):
        super().__init__(id,holder_name)
        self.overdraft_limit=1000  
    def withdraw(self,amount): #polymorphism
        print("###current Account ###")
        if self._balance+self.overdraft_limit>=amount:
            self._balance-=amount
            print("withdrawal successful")
        else:
            print(f"Asked amount is: {amount}")
            print("insufficient balance")
def menu():
    print("\n\n -------------Banking System-----------")
    print("1. Create Saving Account")
    print("2. Create Current Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Calculate Intrest")
    print("7. Exit")
while True:
    menu()
    choice=int(input("Please enter your choice: "))
    if choice==1:
        id=int(input("enter your ID: "))
        holder_name=input("Enter holder Name: ")
        saving=SavingsAccount(id,holder_name)
        print("savings account created Suceessfully!!")
    elif choice==2:
        id=int(input("Enter your ID: "))
        holder_name=input("Enter holder name: ")
        current=CurrentAccount(id,holder_name)
        print("current account created succesfully!!")
    elif choice==3:
        account_id=int(input("enter Account id: "))
        if account_id==saving.id:
            amount=float(input("Enter deposit amount: "))
            saving.deposit(amount)
        elif account_id==current.id:
            amount=float(input("Enter deposit amount: "))
            current.deposit(amount)
        else:
            print("Account not found please create your account!!!")
    elif choice==4:
        account_id=int(input("Enter account ID: "))
        if account_id==saving.id:
            amount=float(input("Enter withdrawal amount: "))
            saving.withdraw(amount)
        elif account_id==current.id:
            amount=float(input("Enter withdrawal amount: "))
            current.withdraw(amount)
        else:
            print("Account not found!! please create your account it")
    elif choice==5:
        id=int(input("Enter your ID: "))
        if id==saving.id:
            saving.check_balance()
        elif id==current.id:
            current.check_balance()
        else:
            print("Account not found")
    elif choice==6:
        account_id=int(input("enter saving account ID: "))
        if account_id==saving.id:
            intrest=saving.calculate_intrest()
            print("Intrest amount:", intrest)
            total=saving._balance+intrest
            print("Total balance after intrest: ",total)
        else:
            print("Savings account not found")
    elif choice==7:
        print("Thankyou for using the Banking System!")
        break
    else:
        print("invalid choice please try again")



    






