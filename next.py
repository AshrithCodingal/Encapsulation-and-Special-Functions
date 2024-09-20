class Value :
    def __init__(self,value,name):
        self.__value=value
        self.__name=name
        
    def printvalue(self):
        print(self.__value)

    def maxprice(self,value):
        self.__value=value
    
    def printname(self):
        print(self.__name)

    def changename(self,name):
        self.__name=name

    

obj=Value(800,"Ashrith")
obj.printname()
obj.changename("Ansh")
obj.printname()