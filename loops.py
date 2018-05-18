def main():
    y=0;#define & assign variable
#While Lopp
    while (y<6):#loop before 5 stop once the value 5 is reached
        print(y)#print the value of y
        y=y+1#increment each time the loop continues
#for loop
    for y in range(10,100):#loop values from the range 10 till 100 once 100 is reached stop loop
        print(y)#prints the value of y
    fquater=["Jan","Feb","Mar","Apr"] #define and assign colllection
    for fq in fquater:#loop over the colllection
        print(fq)#print element by element from colllection
    for y in range(20,40):#loop values from the range 20 till 40 once 40 is reached stop loop
        #if(y==21):break #condition if loop reached 21 stop loop
        #print (y)#print y
        if(y%2==0):continue #if the y value divided by 2 is equal to zero continue loop
        print(y)#print y value
    for q,fq in enumerate(fquater):#get the values & indexes from the colllection
        print (q,fq)  #print indexes & values 

if __name__ =="__main__":
    main()
