class Checkbook:
    """
    A simple checkbook class that allows deposit, withdrawal, and balance checking.

    Attributes:
    balance (float): The current balance in the checkbook.

    Methods:
    deposit(amount): Adds the specified amount to the balance.
    withdraw(amount): Deducts the specified amount from the balance if sufficient funds exist.
    get_balance(): Prints the current balance.
    """
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds the specified amount to the checkbook balance.

        Parameters:
        amount (float): The amount to deposit.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Deducts the specified amount from the checkbook balance if there are sufficient funds.

        Parameters:
        amount (float): The amount to withdraw.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance in the checkbook.

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to run the checkbook application.

    Prompts the user for actions (deposit, withdraw, balance, exit) and handles input validation.

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Exiting the checkbook. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount must be a positive number.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount must be a positive number.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please enter 'deposit', 'withdraw', 'balance', or 'exit'.")


if __name__ == "__main__":
    main()

