class Student :
    def __init__(self,name,rollnum):
        self.__name=name
        self.__rollnum=rollnum
    def printname(self):
        print(self.__name)

    def printrollnum(self):
        print(self.__rollnum)


obj=Student("Ashrith",13)
obj.printname()
obj.printrollnum()



