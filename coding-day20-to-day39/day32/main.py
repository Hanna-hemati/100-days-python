# import smtplib
# import os
#
# my_mail = os.getenv("my_mail")
# my_pass = os.getenv("my_pass")
# to_mail = os.getenv("to_mail")
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_mail, password=my_pass)
#     msg = "Subject: Test Mail\n\nHello Hanna"
#     connection.sendmail(from_addr=my_mail, to_addrs=to_mail, msg=msg)
#

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2003, month=5, day=5, hour=12)
print(date_of_birth)

