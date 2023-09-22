#
class BankAccount:
    def _init_(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}"
        else:
            return "Invalid deposit amount. Please enter a positive amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}"
        elif amount > self.__account_balance:
            return "Insufficient funds."
        else:
            return "Invalid withdrawal amount. Please enter a positive amount."

    def display_balance(self):
        return f"Account balance for {self._account_holder_name}: ₹{self._account_balance}"

# Testing the BankAccount class
if _name_ == "_main_":
    account1 = BankAccount("123456789", "Ganeshkumar", 1000)

    print(account1.display_balance())
    print(account1.deposit(500))
    print(account1.withdraw(200))
    print(account1.withdraw(1500))
    print(account1.display_balance())