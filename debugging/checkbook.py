class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        try:
            self.balance += float(amount)
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()