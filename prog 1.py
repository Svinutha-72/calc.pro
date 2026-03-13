from abc import ABC, abstractmethod

class ATMBase(ABC):
    @abstractmethod
    def check_balance(self):
        pass
    @abstractmethod
    def deposit(self): 
        pass
    @abstractmethod
    def withdraw(self):
        pass

class ATM(ATMBase):
    def __init__(self):
        self.__balance = 10000
        self.transactions = [] 

    def check_balance(self):

        
        print("Your balance:", self.__balance)

    def deposit(self): 
        amount = int(input("Enter amount to deposit:"))
        self.__balance = self.__balance + amount
        self.transactions.append("Deposited " + str(amount))
        print("Deposit successful")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw:"))
        if amount <= self.__balance:
            self.__balance = self.__balance - amount 
            self.transactions.append("Withdraw " + str(amount)) 
            print("Please collect your money")
        else:
            print("Insufficient balance")

    def show_transactions(self): 
        print("Transaction history")
        for t in self.transactions:
            print(t)


atm = ATM()
while True:
    print("\n===== ATM MENU =====")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transactions")
    print("5. Exit")
    
    
    choice = int(input("Enter your choice:")) 
    
    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        atm.deposit() 
    elif choice == 3:
        atm.withdraw()
    elif choice == 4:
        atm.show_transactions() 
    elif choice == 5:
        print("Thank you for using ATM")
        break 
    else:
        print("Invalid option")

