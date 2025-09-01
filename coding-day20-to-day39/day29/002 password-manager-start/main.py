from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def generate_password():
    # password generator
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_symbol + password_numbers

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# save password
# "a" - Append - will create a file if the specified file does not exists
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website or email or password == []:
        messagebox.showerror(message="Your info did not Approved")
    else:
        messagebox.showinfo(title="System Message", message="Your info Approved")

        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.pack()
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "hanna@ht.com")
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, columnspan=1)


# buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()

