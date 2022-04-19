#Create a function that lets the user put in their date of birth, and tell them happy birthday if it's today.

def date():
    from datetime import datetime, date
    
    #name of user
    username = str(input("What is your name? "))

    #input for first date
    y1,m1,d1 = [int(x) for x in input("Enter birthday(yyyy/mm/dd): ").split('/')]
    b1 = date(y1,m1,d1) 

    #input for second date
    y2,m2,d2 = [int(x) for x in input("Enter today's date(yyyy/mm/dd): ").split('/')]
    b2 = date(y2,m2,d2) 

    #date checks
    if m1 == m2 and d1 == d2:
        return "Happy Birthday " + username
    else: 
        return "Enjoy your day"

date()