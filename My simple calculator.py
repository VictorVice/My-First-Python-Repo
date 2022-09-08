
def add(a, b):
    x = a + b
    return x


def mul(a, b):
    y = a * b
    return y


def sub(a, b):
    z = a - b
    return z


def div(a, b):
    h = a / b
    return h


def rem(a, b):
    s = a % b
    return s


print("WELCOME TO MY SIMPLE CALCULATOR")

ans = input("DO YOU WANT TO CARRY OUT A MATHEMATICAL OPERATION? (y for yes, n for no) ").lower()

while ans == "y":
    user = input(
        "What operation do you want to perform? \n'a' for addition,'s' for Subtraction,'m' for Multiplication,"
        "'d' for Division,'r' for Remainder ")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    user.lower()

    
    input_correct = True
    if user == "a":
        input_correct = True
        addition = add(a, b)
        print(f"{a} + {b} = {addition}")
    elif user == "s":
        input_correct = True
        subtraction = sub(a, b)
        print(f"{a} - {b} = {subtraction}")
    elif user == "m":
        input_correct = True
        multiplication = mul(a, b)
        print(f"{a} * {b} = {multiplication}")
    elif user == "d":
        input_correct = True
        division = div(a, b)
        print(f"{a} / {b} = {division}")
    elif user == "r":
        input_correct = True
        remainder = rem(a, b)
        print(f"{a} % {b} = {remainder}")
    else:
        input_correct = False
        break

    ans = input("Do you want to continue?(y/n)")
