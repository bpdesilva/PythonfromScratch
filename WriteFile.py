def main():
    someFile = open("example.txt","w+")#create or find file example.txt
    for x in range(20):#loop through 20x
        someFile.write("The line number is %d\r\n" % (x+1))#write values into the file
    someFile.close()#close the file

if __name__ =="__main__":
    main()
