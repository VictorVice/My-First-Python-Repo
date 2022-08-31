balance = 0
names_dict = {}


def account_creation():
    """Function for account creation """
    name = input("Enter your names here: ")
    pin = int(input("Enter a five-digit pin: "))
    re_entry = int(input("Re-enter your pin here: "))
    while pin != re_entry:
        re_entry = int(input("Your input doesn't match your pin. Please enter your pin: "))
    names_dict[name] = [pin, balance]
    return names_dict


def account_balance():
    """Function to check the user's account balance"""
    count = 5
    name = input("Enter your name: ")
    pin = int(input("Enter your 5 digit pin: "))

    while name not in names_dict:
        print("Incorrect name.")
        name = input("Enter correct name: ")
        while count != 0:
            while pin != names_dict[name][0]:
                pin = int(input("Incorrect pin. You have {count} attempts left."))
                count -= 1
    print(f"{name}'s balance is {names_dict[name][1]}")
    return


def withdrawal():
    """Function that enables the user to withdrawal money from their account."""
    name = input("Enter the name of the account you want to withdrawal from: ")
    pin = int(input("Enter your five-digit pin: "))
    amount = int(input("Enter the amount of money you want to withdraw: "))
    
    if amount > names_dict[name][1]:
        print("There is insufficient funds to complete this transaction.")
        amount = int(input("Enter a less amount amount to be able to withdraw from this account: "))

    attempts = 5
    if pin != names_dict[name][0]:
        while attempts != 0:
            pin = int(input("Incorrect pin. You have {count} attempts left."))
            attempts -= 1
    
    names_dict[name][1] -= amount
    print(f"{name},you have withdrawn {amount}. Your account balance is {names_dict[name][1]}")
    return names_dict


def deposit():
    """Function that enables the user to deposit on their account."""
    name = input("Enter the name of the account you want to deposit on: ")
    amount = int(input("Enter the amount of money you want to deposit: "))
    names_dict[name][1] += amount
    return names_dict


def system():
    """Function that runs the whole system."""
    option_entry = int(
        input("To create a new account press 1.\nTo deposit,press 2.\nTo check account_balance press 3.\nTo "
              "withdrawal money from your account,press 4: "))
    if option_entry == 1:
        account_creation()
    elif option_entry == 2:
        deposit()
    elif option_entry == 3:
        account_balance()
    elif option_entry == 4:
        withdrawal()
    else:
        print("Incorrect entry:")
        option_entry = int(input("Enter a valid input: "))
    return


print("Welcome to Solo's mobile money system")
users_name = input("Enter your name here: ")
print("Hello" + " " + users_name)
question = input("Do you want to carry out a transaction (yes/no): ").lower()

while question == "yes":
    system()
    question = input("Do you want to carry out another transaction (yes/no): ").lower()
