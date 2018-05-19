from datetime import date #import date
from datetime import time #import time
from datetime import datetime #import datetime

def main():
    theday = date.today() #get the system date
    print ("The Date is ",theday) # print the date
    print ("The Date Componets ",theday.day,theday.month,theday.year)#the date Componet by Componet & print
    print ("The Weekday Number is ",theday.weekday()) #print the index of the number of day of the week
    now = datetime.now() # get the system date and time
    print("The date & time now is ",now) # print date & time
    time = datetime.time(datetime.now()) #get the system time
    print("The time now to the second is ",time) # print the system time
    Weekdays = date.weekday(now) #get the date index
    theDays=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"] #define & assign array
    print ("The day today is %d" % Weekdays) # print the index of week
    print ("The day today is "+theDays[Weekdays]) # print the day after getting index

if __name__ == "__main__":
    main()
