# Bank account
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Your account balance is ${self.balance}")


# Create a bank account with an initial balance of $1000
account = BankAccount(1000)

while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        amount = float(input("Enter the deposit amount: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter the withdrawal amount: "))
        account.withdraw(amount)
    elif choice == '3':
        account.display_balance()
    elif choice == '4':
        print("Thank you for using our banking system.")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")