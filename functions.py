#defines a function
def firstFunction():
    #some code of the function
    print("This is a function being printed out")#prints out the statement

firstFunction() #calls out the function firstFunction and executes it's code
print (firstFunction()) #calls out the function firstFunction and executes it's code since there is no return value none is printed to indicate that
print (firstFunction) #since functions in pythons are objects the hexadecimal value printed is address of that object

#defines a function
def secfunction(t1,t2):#passes in two arguments
    #some code of the function
    print(t1," ",t2)#prints out the values

secfunction(40,60)#calls out the function secfunction and executes it's code
print (secfunction(40,60))#call the function passes in the arguments and executes it's code

#defines a function
def squared(k):
     return k*k #mulitplies the arguments to get the squared results and returns values

print (squared(2))#parsed in the argument and print the value

#defines a function
def power(num, m=4):#passes in two arguments one with assigned values
    result=4;#variable defnition and assignment
    for i in range(m):#for loop to through value in m
        result = result*num #multiple with the arguments and parsed values
    return result #returns value

print (power(2))#parsed in an argument and prints the value 64
print (power(2,3))#parsed in an arguments and prints the value 32
print (power(m=3,num=2))#parsed in an arguments and prints the value 32

#defines a function
def addMulitple(*args):#parsed in mulitple the arguments
    result=0;#variable defnition and assignment
    for v in args:#for loop to through arguments
        result= result+v#adds with the arguments and parsed values
    return result#returns value

print (addMulitple(2,4,6,8,10))#parsed in an argument and prints the value 30
