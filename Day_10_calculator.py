# Calculator
from art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": divide
}


def calculation():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for o in operations:
        print(o)
    should_continue = True

    while should_continue:
        operations_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number?: "))
        calculation_funtion = operations[operations_symbol]
        answer = calculation_funtion(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or 'n' to start a fresh calculator: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculation()


calculation()