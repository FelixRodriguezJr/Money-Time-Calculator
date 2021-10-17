from datetime import datetime
from datetime import timedelta

import math
import sys

inputY = "Y"

while str(inputY) == "Y":
    try:
        print("")
        Begindatestring = str(input("Enter date as YYYY-MM-DD: "))
        g = float(input("Enter the Goal Amount: "))
        p = float(input("Enter the Payment Amount: "))
        h = float(input("Enter the Hours per week: "))
    except ValueError:
        print("Use the correct values!")
        sys.exit()

    print("")

    value = g / ((p * h) / 7)

    # taking input as the date
    #Begindatestring = "2020-10-11"

    # carry out conversion between string
    # to datetime object
    Begindate = datetime.strptime(Begindatestring, "%Y-%m-%d")

    # print begin date
    #print("Beginning date")
    #print(Begindate)

    # calculating end date by adding 10 days
    Enddate = Begindate + timedelta(days=value)

    # printing end date
    print("Estimated Date")
    print(Enddate)
    print("")

    inputY = (input("Try again? <Y/N>: ").upper())[0]