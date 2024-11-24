class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance 

    @property
    def balance(self):
        """Getter for the account balance."""
        return self._balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Invalid withdrawal amount. Check your balance.")
account = BankAccount("Alice", 500)

print("----------------")
print("Account Holder:", account.account_holder)
print("Balance:", account.balance)

print("----------------")
account.deposit(200)
print("After depositing $200:")
print("Balance:", account.balance)

print("----------------")
account.withdraw(300)
print("After withdrawing $300:")
print("Balance:", account.balance)

print("----------------")
account.withdraw(500)
print("After trying to withdraw $500:")
print("Balance:", account.balance)