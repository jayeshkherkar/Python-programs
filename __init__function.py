class robin:
    x=5                        # class variable
    y=6
    def __init__(self):
        self.a = int(input("Enter the number = "))   # here "a" is instance variable
        print(self.a)
t1 = robin()                    #instance object
print(t1)

#Alternate method in which we make instance object variable

class robin:
    x=5                        # class variable
    y=6
    def __init__(self,b):
        self.a = b   # here "a" is instance variable
        print(self.a)
t1 = robin(6)   #instance object
t2 = robin(7)
print(t1,t2)

