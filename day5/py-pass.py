import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
           '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '~', '`']
print("welcome to the PyPassword generator!")
nr_alphabets = int(input("how many letters would you like in your password?\n"))
nr_numbers = int(input(f"how many number would you like to add?\n"))
nr_symbol = int(input(f"how many symbols would you like to add?\n"))

password = ""

for ch in range(1, nr_alphabets + 1):
    random_ch = random.choice(alphabets)

for ch in range(1, nr_alphabets + 1):
    random_ch = random.choice(numbers)
    password += random_ch

for ch in range(1, nr_alphabets + 1):
    random_ch = random.choice(symbols)
    password += random_ch

print(password)