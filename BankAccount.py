class BankAccount(object):                                  #this is the base class which other classes will be derived

    def __init__(self, accName, accNumber, balance):
        self.accName = accName;
        self.accNumber = accNumber;                         #Ensure correct Object state through Encapuslation
        self.balance = balance;

    def getAccountName(self):
        return self.accName;                                #Object getters and setters for any required instance variable

    def getAccountNumber(self):
        return self.accNumber;

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if (amount > 0):
            self.balance = self.balance + amount;
            return True;
        else:
            return False;
    def withdraw(self, amount):
        if(amount > self.balance):
            return False;
        else:
            self.balance = self.balance - amount;
            return True


