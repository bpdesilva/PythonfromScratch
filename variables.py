i=2; #variable declaration & intialization
print (i) # prints the value of i

i="Yay! We redecalred this variable." #redeclaring the variable
print (i)# prints the value of i

print ("String concatation works like " +str(1))#string concatation & integer conversion

x=8; #global variable

def doSomething():
    #to make this global
    #global x
    x="Some Value"#local variable
    print (x)

doSomething()#value would be "Some Value"
print (x)##value would be 8
#if x is globally defined inside of the function the new value for both the variable instances would be "Some Value"

del x #removes the memory allocation for the variable and removes the variable from the execution scope
print (x) #error would be printed to indicate x is not defined in any scope of the program this is due to the 21st line added to the program
