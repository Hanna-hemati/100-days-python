import random
import smtplib
import datetime
import os
import pandas as pd

my_mail = "hanna.hematii@gmail.com"
my_pass = "keinjertojoetjab"

birthday_data = pd.read_csv("birthday_data.csv")


def send(to_email):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=my_pass)
        # متن تبریک از فایل
        with open("whishs.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        options = [line.strip().strip('"') for line in lines if line.strip()]
        choice = random.choice(options)

        # ساخت پیام ایمیل
        subject = "Birthday Wishes 🎉"
        msg = f"Subject: {subject}\n\n{choice}"

        connection.sendmail(
            from_addr=my_mail,
            to_addrs=to_email,
            msg=msg.encode("utf-8")  # پشتیبانی کاراکتر فارسی
        )
    print(f"ایمیل به {to_email} ارسال شد ✅")


today = datetime.date.today()
for index, row in birthday_data.iterrows():
    # چک کردن ماه و روز
    if row['month'] == today.month and row['day'] == today.day:
        send(row['email'])
