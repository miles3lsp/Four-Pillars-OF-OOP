class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Private attribute hidden from outside

    # Getter method to access private data safely
    def get_balance(self):
        return self.__balance

    # Setter method to modify private data safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Amount must be positive!")

account = BankAccount("Alex", 1000)
account.deposit(500)