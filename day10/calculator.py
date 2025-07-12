def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

accumulate = True

while accumulate:
    num1 = float(input("What is your first num?..."))
    for symbol in operation:
        print(symbol)
    operation_symbol = input("pick an operation")
    num2 = float(input("what is your second num?"))
    answer = operation[operation_symbol](num1, num2)
    print(f"{num1}{operation_symbol}{num2} = {answer}")

    choice = input(f"Type 'y' if you want continue, otherwise type 'n'.")

    if choice == "y":
        num1 = answer
    else:
        accumulate = False
        print("Bye Bye")