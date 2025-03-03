class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = "3542"
        self.history = []

    
    def Amount_Deposit(self, pin):
        if(pin == self.pin):
            amount = int(input(" Enter the amount you want to deposit: "))
            self.balance += amount
            print(" The Amount has Successfully been deposited ")
            self.history.append(f" {amount}INR has been deposited ")
        else:
            print(" Error: You have Entered a wrong pin ")
    
    def Account_Balance(self, pin):
        if(pin == self.pin):
            print(f" The account balance is {self.balance}INR")
            self.history.append(" The Account balance has been checked ")
        else:
            print(" Error: You have Entered a wrong pin ")

    def Amount_Withdraw(self, pin):
        if(pin!=self.pin):
            print(" Error: You have Entered a wrong pin ")
            return
        amount = int(input(" Enter the amount you want to withdraw: "))
        if(self.balance < amount):
            print(" Insufficient Balance ")
        else:
            self.balance -= amount
            print(f" You have successfully withdrawn: {amount}INR")
            self.history.append(f" you withdrew {amount}INR from the account ")
    
    def Pin_Change(self,oldpin):
        if(oldpin == self.pin):
            newpin = input(" Enter the new pin: ")
            self.pin = newpin
            print(" New pin has successfully been changed ")
            self.history.append(" The old pin is changed to new pin ")
        else:
            print(" Error: You have Entered a wrong pin ")
        
    def Transaction_History(self, pin):
        if(pin == self.pin):
            print("\n Transaction History \n ----------- -------")
            i = 0
            for transaction in self.history:
                i+=1
                print(f" {i}. {transaction}")
        else:
            print(" Error: You have Entered a wrong pin ")

Atm = ATM()

choice = 1

print('\n\n\tATM Machine \n\t--- -------')

while(choice == 1):

    print("\n\t  options\n\t  -------\n\n 1. Cash Deposit \n 2. Account Balance \n 3. Cash Withdrawl \n 4. Change the pin \n 5. Transaction History \n\n")


    option = int(input(" Enter the option: "))
    
    if(option == 1):
        pin = input(" Enter the pin: ")
        Atm.Amount_Deposit(pin)
        print()
    elif(option == 2):
        pin = input(" Enter the pin: ")
        Atm.Account_Balance(pin)
        print()
    elif(option == 3):
        pin = input(" Enter the pin: ")
        Atm.Amount_Withdraw(pin)
        print()
    elif(option == 4):
        pin = input(" Enter the pin: ")
        Atm.Pin_Change(pin)
        print()
    elif(option == 5):
        pin = input(" Enter the pin: ")
        Atm.Transaction_History(pin)
        print()
    else:
        print(" You have entered an invalid option \n")

    choice = int(input(" if You want to do another transaction Enter 1 else enter any number except 1: "))

print("\n\t Thank you for using our ATM Machine \n")