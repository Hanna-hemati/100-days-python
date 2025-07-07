

n1 = int(input("write your fist num..."))
n2 = int(input("write your second num..."))
op = input("""chose from these operation:
+
-
*
/
""")

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


if op == "+":
    print(operation["+"](n1, n2))
elif op == "-":
    print(operation["-"](n1, n2))
elif op == "*":
    print(operation["*"](n1, n2))
elif op == "/":
    print(operation["/"](n1, n2))
else:
    print("the input is invalid")


