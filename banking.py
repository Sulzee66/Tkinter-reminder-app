balance = 0
def deposit(amount):
    global balance
    balance += amount
    print("Deposit successful. Current balance:", balance)
def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print("Withdrawal successful. Current balance:", balance)
def check_balance():
    print("Current balance:", balance)
while True:
    print("\n======= Banking System =======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        deposit_amount = float(input("Enter the deposit amount: "))
        deposit(deposit_amount)
    elif choice == 2:
        withdraw_amount = float(input("Enter the withdrawal amount: "))
        withdraw(withdraw_amount)
    elif choice == 3:
        check_balance()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")