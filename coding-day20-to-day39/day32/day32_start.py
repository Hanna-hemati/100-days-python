import random
import smtplib
import datetime as dt
import os

my_mail = os.getenv("my_mail")
my_pass = os.getenv("my_pass")
to_mail = os.getenv("to_mail")

now = dt.datetime.now()
date_of_week = now.weekday()

def send():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=my_pass)
        with open("quotes.txt", "r") as f:
            lines = f.readlines()
        options = [line.strip().strip('"') for line in lines if line.strip()]
        choice = random.choice(options)
        connection.sendmail(from_addr=my_mail, to_addrs=to_mail, msg=choice)


if date_of_week == 1:
    send()
else:
    print("it's not tuesday")

