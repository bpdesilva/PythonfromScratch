#Defines function
def main():
    p,q=100,1000 #variable declaration and assignment
    if(p<q): #condition if p is less than y
        str = "p is less than y"
    elif(p==q): #second condition if p is equal to q
        str="p is equal to q"
    else: # final exit condition if p is greater than q
        str="p is greater than q"
    print(str)#prints the result

    #one line conditional (if this then that or "x if Z else Y")
    ss="p is less than y" if(p<q) else "p is greater than or equal to q"
    print (ss)

#validates the program for the desired function for execution
if __name__ =="__main__":
    main()#calls the function
