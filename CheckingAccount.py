from BankAccount import BankAccount

class CheckingAccount(BankAccount):             # Checking Account Inherits from Bank Account
    transactionCount = 0;
    number_fee = 3;                             #Class Attributes different from instance variables
    transaction_fee = 2.0;

    def __init__(self):
        self.transactionCount = 0;              #Encapsulation: Talking of State

    def deposit(self, amount):                  #Polymorphism: Method Overide enables the object to exist in many forms
        if(self.deposit(amount)):
            self.transactionCount = self.transactionCount + 1;
            return True;
        else:
            return False;

    def withdraw(self, amount):                 #Polymorphism: Method Override enables object to exist in various forms
        if(self.withdraw(amount)):
            self.transactionCount = self.transactionCount + 1;
            return True;
        else:
            return False;

    def deductFee(self):
        if(self.transactionCount > self.number_fee):
            fees = self.transaction_fee * (self.transactionCount - self.number_fee)
            if(self.withdraw(fees)):
                self.transactionCount = 0;