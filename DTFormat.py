from datetime import datetime #import date & time

def main():
    current = datetime.now() #get the system date & time
    print (current.strftime("%Y"))# print year with century
    print (current.strftime("%y"))# print last two digits of the year
    print (current.strftime("%a, %d, %B, %Y"))#print date ,Time & month
    print (current.strftime("%c"))#print local date,month , year & time
    print (current.strftime("%x"))#print date
    print (current.strftime("%X"))#print time 24 hour clock format
    print (current.strftime("%I:%S:%M %p"))#print time 12 hour clock format also prints seconds
    print (current.strftime("%H:%M"))#prints time in 24 hour clock format

if __name__=="__main__":
    main()
