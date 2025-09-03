from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamadoro")
window.config(padx=50, pady=50, bg=PINK)

title_label = Label(text="TIMER", fg=GREEN, bg=PINK, font=(FONT_NAME, 30))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato)
canvas.create_text(100, 100, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✅")


window.mainloop()
