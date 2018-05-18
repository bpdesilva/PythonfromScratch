class someClass():#class definition
    def someMethod(self):#define method
        print ("This is a message from someMethod in someClass..")#method code

    def doMethod(self,str):#define method parse arguments
        print ("This is a message from doMethod in someClass "+str)#method code

class someOtherClass(someClass):#inheritance
    def doMethod(self):#define method
        print("This is a message from didSomething in someOtherClass..")#method code

    def doingSomething(self):#define method
        someClass.someMethod(self)#
        print("This is a message from doingSomething in someOtherClass..")#method code

#main function
def main():
    a = someClass()#instance of the class or creating an object of that class
    a.someMethod()#accessing method for execution
    a.doMethod("This is another string")#accessing method for execution
    b = someOtherClass() #creating an instance of the class
    b.doingSomething()#accessing method for execution
    b.doMethod()#accessing method for execution - overriding

if __name__ =="__main__":
    main()#call main
