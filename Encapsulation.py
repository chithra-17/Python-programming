# A constructor is a special method used to initialize object values.
class Bank:

    def __init__(self,balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("New Balance:", self.balance)

b1 = Bank(1000)
b1.deposit(500)