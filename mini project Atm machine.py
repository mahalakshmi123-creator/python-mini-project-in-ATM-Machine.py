balance = 10000  # Initial balance of ₹10,000


def show_menu():
    print("**** ATM MENU ****")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def check_balance():
    print("Available balance",balance)

def deposit():
    global balance
    amount = int(input("Enter amount to deposit" ))
    if amount is None:
        return
    balance += amount
    print("amount:10000} deposited successfully")
    check_balance()


def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw"))
    if amount is None:
        return
    if amount > balance:
        print("Insufficient funds")
        return
    balance -= amount
    print(amount,"Amount withdrawn successfully")
    check_balance()


def choice():
    while True:
        show_menu()
        choice = input("Select an option (10000) ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")
choice()

