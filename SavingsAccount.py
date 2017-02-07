from BankAccount import BankAccount

class SavingsAccount(BankAccount):                                  #SavingsAccount inherits from Bank Account

    def __init__(self, rate):
        self.interestrate = rate;                                   #Encapsulation: Talking of state of the Object
        self.interest = None

    def add_interest(self):
        self.interest = self.getBalance() * self.interestrate / 100; #get Balance method from inherited Class
        self.deposit(self.interest);
