def main():
    someFile = open("example.txt","r")#read file
    if someFile.mode=='r': #if read access
        fileStuff =someFile.read() #read the file
        print(fileStuff) #print the file content
    filesList = someFile.readlines() #read all the lines
    for q in filesList: #loop through the file
        print(q) # print the lines
if __name__=="__main__":
    main()
