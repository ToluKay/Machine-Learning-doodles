#Create a function that lets the user put in their date of birth, and tell them happy birthday if it's today.

import datetime
def birthday():
    username = str(input("What is your name? "))
    bday = input('When is your birthday? (In MM/DD)')
    birthdate = datetime.datetime.strptime(bday,"%m/%d")
    today_date = datetime.date.today()
    print(today_date)

    if birthdate == today_date:
        return("Happy Birthday" + username + "!")
    else:
        return("Enjoy your day.")

birthday()