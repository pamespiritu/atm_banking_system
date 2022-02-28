from banking_pkg.account import show_balance, deposit, withdraw, logout

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = str(0)
print(name , "has been registered with a starting balance of $" , balance)

print("          === Automated Teller Machine ===          ")
while True:
    name_to_validate = input("Enter username: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")
        break

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    
    if option == "1":
        show_balance(balance)
    elif option == "2":
        balance = deposit(balance)
        show_balance(balance)
    elif option == "3":
        balance = withdraw(balance)
        show_balance(balance)
    elif option == "4":
        logout(name)
        break
    