def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    
    if amount < 0:
        print("You can't deposit a negative amount")
        return 0

    else:
        return amount

def withdraw():
    amount = float(input("Enter the amount to withdraw: "))
    if withdraw > amount:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("You can't withdraw a negative amount")
        return 0
    else:
        return amount


balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1 - Show Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_balance()

    elif choice == '2':
        balance += deposit()
    
    elif choice == '3':
        balance -= withdraw()
    
    elif choice == '4':
        is_running = False


print("Goodbye!")