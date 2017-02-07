from BankAccount import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, rate):
        self.interestrate = rate;
        self.interest = None

    def add_interest(self):
        self.interest = self.getBalance() * self.interestrate / 100;
        self.deposit(self.interest);
