from datetime import datetime
from datetime import timedelta
import sys

# Initializing while loop to repeat the operation until user decides to quit.

inputY = "Y"

while str(inputY) == "Y":
    try:
        print("")
        Begindatestring = str(input("Enter date as YYYY-MM-DD: "))
        goal = float(input("Enter the Goal Amount: "))
        pay = float(input("Enter the Payment Amount: "))
        hours = float(input("Enter the Hours per week: "))
    except ValueError:
        print("Use the correct values!")
        sys.exit()

    print("")

    # calculating the time elapsed for goal to be reached

    timeElapsed = goal / ((pay * hours) / 7)

    # taking input as the date
    # Begindatestring = "YYYY-MM-DD"

    # carry out conversion between string
    # to datetime object
    BeginDate = datetime.strptime(Begindatestring, "%Y-%m-%d")

    # print begin date
    print("Start Date")
    print(BeginDate)
    print("----------")

    # calculating end date by adding 10 days
    EndDate = BeginDate + timedelta(days=timeElapsed)

    # printing end date
    print("Estimated Date")
    print(EndDate)
    print("")

    inputY = (input("Try again? <Y/N>: ").upper())[0]