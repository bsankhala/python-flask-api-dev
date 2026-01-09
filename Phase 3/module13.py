accounts = {}

def create_account(name):
    accounts["name"] = name
    accounts["balance"] = 0
    return "Account created successfully"

def deposit(amount):
    accounts["balance"] += amount
    return "Amount deposited successfully"

def withdraw(amount):
    if amount > accounts["balance"]:
        return "Insufficient balance"
    accounts["balance"] -= amount
    return "Withdrawal successful"

def check_balance():
    return accounts["balance"]

while True:
    print("\n1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        print(create_account(name))

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        print(deposit(amount))

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        print(withdraw(amount))

    elif choice == 4:
        print("Current balance:", check_balance())

    elif choice == 5:
        print("Thank you for using banking system")
        break

    else:
        print("Invalid choice")
