def show_balance(balance):
    print("Your available balance is: " , float(balance))

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return (float(balance) + float(amount))

def withdraw(balance):
    amount_withdraw = input("Enter amount to withdraw: ")
    return (float(balance) - float(amount_withdraw))

def logout(name):
    print("Goodbye!" , name)
