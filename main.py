##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import random
import datetime as dt

# get the current details of today
now = dt.datetime.now()
month = now.month
day = now.day
birthdays = pandas.read_csv("birthdays.csv")

my_email = "pythonlearncode114@gmail.com"
password = "ykiivixaeyphfpam"

# gets the name that matches the birthday date
for (index, value) in birthdays.iterrows():
    if value.day == day and value.month == month:
        letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
        celebrant = value["name"]

# open the randomly selected letter and replace the name with the name that corresponds with the birthday
with open(letter, mode="r+") as mail:
    read = mail.readlines()
    line_one = read[0].replace("[NAME]", f"{celebrant}")
with open("letter_to_send.txt", mode="w") as mail_send:
    mail_send.write(line_one)
    listToStr = ''.join(map(str, read[1:]))
    mail_send.write(listToStr)

# start connection to the email server
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    # open the letter to send and sends it to the recepient
    with open("letter_to_send.txt") as birthday_wishes:
        birthday_mail = birthday_wishes.read()
        connection.sendmail(from_addr=my_email, to_addrs="pythontutorial40@gmail.com",
                            msg=f"Subject: Happy Birthday\n\n{birthday_mail}"
                            )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




