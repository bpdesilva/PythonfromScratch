import os #import os module
from os import path #get paths in OS
import datetime #import date time module
from datetime import date , time, timedelta #get date time
import time

def main():
    print(os.name) #print out the os kernal name
    print("File exists "+str(path.exists("example.txt"))) #check if file is present
    print("File type is "+str(path.isfile("example.txt"))) #validate file tipe
    print("File is a Directory "+str(path.isdir("example.txt"))) #print file file location
    print("The real file path "+str(path.realpath("example.txt"))) #print file file location with formatting
    print("The real file path "+str(path.split(path.realpath("example.txt")))) # Full path to file location

    tm = time.ctime(path.getmtime("example.txt"))#get File editied time
    print (tm) #print editied time and date
    print(datetime.datetime.fromtimestamp(path.getmtime("example.txt"))) #print in datetime format 

    #tnd = datetime.datetime.now()-datetime.datetime.fromtimestamp(path.getmtime("example.txt")
    #print("It was "+str(tnd)+" the file was last changed.")
    #print("Or, " +str(tnd.total_seconds())+" seconds")

if __name__=="__main__":
    main()
