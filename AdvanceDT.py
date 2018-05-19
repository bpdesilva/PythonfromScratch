from datetime import date #import date
from datetime import time #import time
from datetime import datetime #import datetime
from datetime import timedelta #

def main():
    print (timedelta(days=365, hours=6,minutes=2))#print out the date time defintion
    print ("Today is "+str(datetime.now()))#print todays date time
    print ("One year from now... "+str(datetime.now() + timedelta(days=365)))#print the date & time from 1 year
    print ("In 2 Weeks & 3 Days..." +str(datetime.now() +timedelta(weeks=2, days=2)))# print the the date & time in 2 weeks & 3 days
    tm = datetime.now() - timedelta(weeks=1)#Calculate time and date
    st = tm.strftime("%A %B %d,%Y")#convert string
    print ("One week ago... " +st)# print string
    td = date.today()#get todays date
    AprilsFool =date(td.year, 4,1)# define date for aprils's fool
    if AprilsFool <td: # check if the values are less than the current date
        print ("April's fools day was %d"%(td-AprilsFool).days) #print by how many days we missed aprils fool
        AprilsFool=AprilsFool.replace(year=td.year+1) #if the date is passed get date for next year
        rm_AprilsFool = abs(AprilsFool-td) #Calculate the days for the next year
        print("Days for April's Fools Day ",rm_AprilsFool.days) # print out the reamining days
if __name__ =="__main__":
    main()
